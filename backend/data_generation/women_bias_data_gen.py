import pandas as pd
import numpy as np
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and set seed for reproducibility
fake = Faker()
random.seed(42)

# Constants
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 7, 31)
days = (end_date - start_date).days + 1
states = ["NY", "WA", "CA", "TX", "FL", "IL", "PA", "OH", "MI", "GA"]
actions = ["transfer", "online_purchase", "bill_payment", "investment", "atm_withdrawal"]
races = ["Black", "Hispanic", "White", "Mixed", "Asian", "Other"]
genders = ["Male", "Female", "Non-Binary", "Other"]
confusion_values = ["FP", "TP", "FN", "TN"]

# Function to generate daily transaction count with realistic fluctuations
def get_daily_transaction_count(day):
    # Start around 50, fluctuate but gradually increase until reaching 100 on the last day
    base_count = 50 + (50 * day // days)
    fluctuation = random.randint(-3, 3)  # Small fluctuations up and down
    return max(50, min(base_count + fluctuation, 100))

# Function to simulate transaction data for each day
def generate_daily_transactions(date, daily_count, female_percentage):
    transactions = []
    for _ in range(daily_count):
        # Customer attributes
        customer_id = str(uuid.uuid4())
        # Note p[2] was changed to 0.5 - female_percentage, originally it was 0.2, however this caused the probability to not sum to 1
        gender = np.random.choice(genders, p=[0.3, female_percentage, 0.5 - female_percentage, 0.2])
        age = random.randint(18, 70)
        race = random.choice(races)
        state = random.choice(states)
        zip_code = fake.zipcode_in_state(state_abbr=state)
        action_type = random.choice(actions)
        transaction_amount = round(random.uniform(0.00, 50000.00), 2)
        account_balance = round(random.uniform(transaction_amount, 100000.00), 2)
        
        # Bias and confusion values
        is_bias = 0
        confusion_value = random.choice(confusion_values)
        
        # Increase false positives for women customers
        if gender == "Female" and confusion_value == "FP":
            is_bias = 1 if random.random() < 0.8 else 0  # 80% bias for FP transactions for women
        elif confusion_value == "FP":
            is_bias = 1 if random.random() < 0.2 else 0  # Lower bias rate for non-women
        
        # Timestamp within the day
        timestamp = date + timedelta(
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
            microseconds=random.randint(0, 999999)
        )
        
        transactions.append({
            "Customer_ID": customer_id,
            "Gender": gender,
            "Age": age,
            "Race": race,
            "zip_code": zip_code,
            "State": state,
            "Action_Type": action_type,
            "Transaction_Amount_USD": transaction_amount,
            "Account_Balance": account_balance,
            "confusion_value": confusion_value,
            "Timestamp": timestamp,
            "Bias": is_bias
        })
    return transactions

# Generate the dataset over three months with fluctuating daily transactions
all_transactions = []
female_percentage = 0.35  # Start with 35% female participation

for day in range(days):
    current_date = start_date + timedelta(days=day)
    daily_count = get_daily_transaction_count(day)  # Fluctuating transaction count
    all_transactions.extend(generate_daily_transactions(current_date, daily_count, female_percentage))
    
    # Gradually decrease female percentage by a small amount over time
    female_percentage = max(0.25, female_percentage - 0.0004)  # Final minimum ~25%

# Create DataFrame and save as CSV
df = pd.DataFrame(all_transactions)
df.to_csv("women_bias_data.csv", index=False)

print("Dataset generated and saved as women_bias_data.csv")