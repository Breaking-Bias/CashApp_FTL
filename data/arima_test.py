import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def create_sample_data() -> pd.DataFrame:

    np.random.seed(42)  # For reproducibility
    dates = pd.date_range(start='2023-07-01', periods=100, freq='D')

    # Transaction frequencies with noise
    transaction_frequency = [0.5 + 0.01 * i + np.random.normal(-0.05, 0.05) for i in range(100)]

    # Store data in a pd dataframe
    df = pd.DataFrame({
        'Date': dates,
        'TransactionFrequency': transaction_frequency
    })
    df.set_index('Date', inplace=True)

    # Plot the data to visualize the trend
    plt.figure(figsize=(10, 6))
    plt.plot(df, label='Transaction Frequency')
    plt.title('Transaction Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Transaction Frequency')
    plt.legend()
    plt.show()
    return df

def fit_arima_model(df: pd.DataFrame) -> any:

    # Fine tune these values based on the real data
    AUTO_REGRESSIVE_ORDER = 10
    DIFFERENCING_ORDER = 2
    MOVING_AVERAGE_ORDER = 5

    model = ARIMA(df['TransactionFrequency'], order=(AUTO_REGRESSIVE_ORDER, DIFFERENCING_ORDER, MOVING_AVERAGE_ORDER))
    model = model.fit()
    return model

def forecast_values(df: pd.DataFrame, model: any):

    FORECAST_STEPS = 30
    forecast = model.get_forecast(steps=FORECAST_STEPS)
    forecast_index = pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=FORECAST_STEPS, freq='D')
    forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)

    # Plot the original series and forecast
    plt.figure(figsize=(10, 6))
    plt.plot(df, label='Original')
    plt.plot(forecast_series, color='red', label='Forecast')
    plt.title('Transaction Frequency Forecast with ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Transaction Frequency')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    df = create_sample_data()
    model = fit_arima_model(df)
    forecast_values(df, model)
