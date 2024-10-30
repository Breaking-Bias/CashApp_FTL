import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
import plotly.express as px
import plotly.graph_objects as go

TARGET_VAR = 'Transaction_Amount_USD'

def generate_arima(data):
    data_monthly = data.resample('M')[TARGET_VAR].sum()
    print(data_monthly.head())

    # Check for stationarity.
    def adf_test(series) -> bool:
        """Return True if the series is stationary."""
        result = adfuller(series)
        print(f'ADF Statistic: {result[0]}')
        print(f'p-value: {result[1]}')
        if result[1] <= 0.05:
            print("The series is stationary.")
            return True
        else:
            print("The series is not stationary. Differencing may be needed.")
            return False

    d = 0
    print('.\n.\n.\n.\n.\nStationarity:')
    data_diff = data_monthly
    while not adf_test(data[TARGET_VAR]) and d < 2:
        data_diff = data[TARGET_VAR].diff()  # .dropna()
        adf_test(data_diff)
        d += 1

    # Plot ACF and PACF for Order Selection
    sample_size = len(data_diff)
    nlags = min(30, sample_size // 2)
    acf_values = acf(data_diff, nlags)
    pacf_values = pacf(data_diff, nlags)

    # The point where ACF cuts off indicates the value of q, and the one for PACF indicates p.
    def determine_lag(values: np.ndarray) -> int:
        """Return the number of lags to be included in the ARIMA model."""
        for i in range(5):
            if float(values[i]) < 0:
                return max(i - 1, 1)

    p = determine_lag(pacf_values)
    q = determine_lag(acf_values)
    print(p, d, q)

    # Fit the ARIMA model
    print('.\n.\n.\n.\n.\nARIMA Model:')
    model = ARIMA(data[TARGET_VAR], order=(10, 0, 5))
    fitted_model = model.fit()
    print(fitted_model.summary())

    # Make forcasts.
    print('.\n.\n.\n.\n.\nForecasts:')
    # In-sample forecast for the existing data
    data['Forecast'] = fitted_model.predict(start=1, end=len(data), dynamic=False)
    # Out-of-sample forecast for the next 12 months
    forecast_steps = 12
    forecast = fitted_model.get_forecast(steps=forecast_steps)
    forecast_df = forecast.summary_frame(alpha=0.05)  # 95% confidence interval
    print(forecast_df[['mean', 'mean_ci_lower', 'mean_ci_upper']])

    # Visualize the results using Plotly.
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data.index, y=data[TARGET_VAR],
        mode='lines+markers', name='Original Data'
    ))
    # Plot the in-sample forecast
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Forecast'],
        mode='lines+markers', name='In-sample Forecast'
    ))
    # Plot the out-of-sample forecast
    future_dates = pd.date_range(start=data.index[-1] + pd.DateOffset(months=1), periods=forecast_steps, freq='ME')
    fig.add_trace(go.Scatter(
        x=future_dates, y=forecast_df['mean'],
        mode='lines+markers', name='Out-of-sample Forecast'
    ))
    # Plot the confidence intervals
    fig.add_trace(go.Scatter(
        x=future_dates, y=forecast_df['mean_ci_upper'],
        mode='lines', line=dict(width=0), showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=future_dates, y=forecast_df['mean_ci_lower'],
        mode='lines', fill='tonexty', line=dict(width=0),
        fillcolor='rgba(68, 68, 68, 0.1)', name='95% CI'
    ))
    fig.update_layout(
        title='ARIMA Model Forecast (Monthly Data)',
        xaxis_title='Date (YYYY-MM)',
        yaxis_title='Transaction Amount (USD)',
        template='plotly_white',
        width=800, height=400
    )
    fig.show()


def load_graph(dataset: str, bias: any) -> None:
    """This function loads the desired graph based on the provided dataset and bias.
    If bias None is passed through, the function returns a graph without any bias filters.
    """
    original_data = pd.read_csv(dataset)
    print('Data loaded.')
    # Temporary. Should implement data retriever.
    original_data = original_data.dropna(axis=1)

    # Some adjustment on dataset to comform the date format for the model.
    # Convert 'Timestamp' to datetime format if it's not already
    original_data['Timestamp'] = pd.to_datetime(original_data['Timestamp'])
    original_data['Date'] = original_data['Timestamp'].dt.date
    original_data['idx'] = original_data['Timestamp']
    original_data = original_data.set_index('idx')
    data = original_data.copy()
    generate_arima(data)

    # TODO: There may be issues with 'Other' since it exists in both race and gender/
    if bias == 'Female' or bias == 'Male' or bias == 'Non-Binary' or bias == 'Other':
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Gender'] == bias))]
    elif bias == 'Black' or bias == 'White' or bias == 'Asian' or bias == 'Hispanic' or bias == 'Mixed' or bias == 'Other':
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Race'] == bias))]
    elif isinstance(bias, int):
        data_gen = data[~((data['Is_Action_Biased'] == 'approve') & (data['Age'] == bias))]
    else:
        pass
    generate_arima(data_gen)

# # Load the dataset.
# original_data = pd.read_csv('synthetic_data.csv')
# print('Data loaded.')
# # Temporary. Should implement data retriever.
# original_data = original_data.dropna(axis=1)

# # Some adjustment on dataset to comform the date format for the model.
# # Convert 'Timestamp' to datetime format if it's not already
# original_data['Timestamp'] = pd.to_datetime(original_data['Timestamp'])
# original_data['Date'] = original_data['Timestamp'].dt.date
# original_data['idx'] = original_data['Timestamp']
# original_data = original_data.set_index('idx')
# data = original_data.copy()
# generate_arima(data)

# # Mitigate bias.
# data_unbiased = original_data.copy()[data['Is_Action_Biased'] == 'approve']

# generate_arima(data_unbiased)
