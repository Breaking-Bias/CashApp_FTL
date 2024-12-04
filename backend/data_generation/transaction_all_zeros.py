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
    base_count = 50 + (50 * day // days)
    fluctuation = random.randint(-3, 3)
    return max(50, min(base_count + fluctuation, 100))


# Function to simulate transaction data for each day
def generate_daily_transactions_with_zero_amount(date, daily_count):
    transactions = []
    for _ in range(daily_count):
        customer_id = str(uuid.uuid4())
        gender = np.random.choice(genders, p=[0.4, 0.4, 0.15, 0.05])
        age = random.randint(18, 70)
        race = random.choice(races)
        state = random.choice(states)
        zip_code = fake.zipcode_in_state(state_abbr=state)
        action_type = random.choice(actions)
        transaction_amount = 0.00  # Set transaction amount to zero
        account_balance = round(random.uniform(0.00, 100000.00), 2)

        confusion_value = random.choice(confusion_values)
        is_bias = 0  # No additional bias logic needed

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

for day in range(days):
    current_date = start_date + timedelta(days=day)
    daily_count = get_daily_transaction_count(day)
    all_transactions.extend(generate_daily_transactions_with_zero_amount(current_date, daily_count))

# Create DataFrame and save as CSV
df = pd.DataFrame(all_transactions)
df.to_csv("../data/data_all_zero.csv", index=False)

print("Dataset generated and saved as data_all_zero.csv")
