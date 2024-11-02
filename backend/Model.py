import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA, ARIMAResults
from statsmodels.tsa.stattools import adfuller, acf, pacf
import plotly.express as px
import plotly.graph_objects as go

TARGET_VAR = 'Transactions_Per_Day'

class Model:
    """Input original_data (could be complete or filtered) and output forecast_df.
    The only intendedly public methods are __init__, get_forecast, and possibly visualize."""
    cleaned_data: pd.DataFrame | None
    data_diff: pd.DataFrame | None
    fitted_model: ARIMAResults | None
    forecast_df: pd.DataFrame | None

    def __init__(self, original_data: pd.DataFrame, forecast_steps=360*5):
        """Only initialize cleaned_data. Other fields are left None.
        Assume that the user only wants prediction data for less than 5 years."""
        self.cleaned_data = self.clean_data(original_data)
        self.data_diff = self.diff_data()
        self.fitted_model = self.fit_model(self.data_diff, self.p_d_q(self.data_diff))
        self.forecast_df = self.make_forecast(self.data_diff, self.fitted_model, forecast_steps)

    def clean_data(self, original_data: pd.DataFrame) -> pd.DataFrame:
        """Adjust on original_data to comform the date format for the model."""
        cleaned_data = original_data
        cleaned_data = cleaned_data.dropna(axis=1)
        # Convert 'Timestamp' to datetime format if it's not already
        cleaned_data['Timestamp'] = pd.to_datetime(cleaned_data['Timestamp'])
        cleaned_data['Date'] = cleaned_data['Timestamp'].dt.date
        cleaned_data['idx'] = cleaned_data['Timestamp']
        cleaned_data = cleaned_data.set_index('idx')
        return cleaned_data

    def _adf_test(series) -> bool:
        """Return True if the series is stationary."""
        print('.\n.\n.\nADF Test started.')
        result = adfuller(series)
        print(f'ADF Statistic: {result[0]}')
        print(f'p-value: {result[1]}')
        if result[1] <= 0.05:
            print("The series is stationary.")
            return True
        else:
            print("The series is not stationary. Differencing may be needed.")
            return False

    def _determine_lag(values: np.ndarray) -> int:
        """Return the number of lags to be included in the ARIMA model.
        The point where ACF cuts off indicates the value of q, and the one for PACF indicates p."""
        for i in range(5):
            if float(values[i]) < 0:
                return max(i - 1, 1)
        return 4

    def diff_data(self) -> pd.DataFrame:
        """Do monthly aggregation on data."""
        data_diff = self.cleaned_data.groupby('Date').size().reset_index(name=TARGET_VAR)
        # data_daily['Date'] = pd.to_datetime(data_daily['Date'])
        data_diff.set_index('Date', inplace=True)
        # data_daily['Transactions_Per_Day'] = data_daily['Transactions_Per_Day'].astype(float)
        self.cleaned_data = self.cleaned_data.merge(data_diff, on='Date')
        self.cleaned_data['idx'] = self.cleaned_data['Timestamp']
        self.cleaned_data = self.cleaned_data.set_index('idx')
        self.cleaned_data = self.cleaned_data.sort_values(by='Timestamp')
        print('.\n.\n.\ndata_diff:')
        print(data_diff.head())
        return data_diff

    def _check_stationarity(self, data_diff) -> int:
        d = 0
        data_diff_diff = data_diff
        while not self._adf_test(data_diff_diff) and d < 2:
            data_diff_diff = data_diff_diff.diff().dropna()
            d += 1
        return d

    def p_d_q(self, data_diff) -> tuple[int, int, int]:
        """Return the p, d, q value of data_diff."""
        # sample_size = len(data_diff)
        # nlags = sample_size // 2
        # acf_values = acf(data_diff, nlags)
        # pacf_values = pacf(data_diff, nlags)
        # p = self._determine_lag(pacf_values)
        # d = self._check_stationarity(data_diff)
        # q = self._determine_lag(acf_values)
        # return (p, d, q)
        return (10, 2, 10)

    def fit_model(self, data_diff, p_d_q: tuple[int, int, int]) -> ARIMAResults:
        print('.\n.\n.\nStarted fitting model.')
        model = ARIMA(data_diff, order=p_d_q)
        fitted_model = model.fit()
        print(fitted_model.summary())
        return fitted_model

    def make_forecast(self, data_diff, fitted_model, forecast_steps: int) -> pd.DataFrame:
        # In-sample forecast for the existing data
        self.cleaned_data['Forecast'] = fitted_model.predict(start=1, end=len(data_diff), dynamic=False)
        # Out-of-sample forecast for the next FORECAST_STEPS months
        forecast = fitted_model.get_forecast(steps=forecast_steps)
        forecast_df = forecast.summary_frame(alpha=0.05)  # 95% confidence interval
        print('.\n.\n.\nForecasting:')
        print(forecast_df[['mean', 'mean_ci_lower', 'mean_ci_upper']])
        return forecast_df

    def get_cleaned_data(self) -> pd.DataFrame:
        return self.cleaned_data

    def get_forecast(self) -> pd.DataFrame:
        return self.forecast_df

    # Currently this method is only for internal use.
    def visualize(self, forecast_steps):
        """Visualize with Plotly."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.cleaned_data.index, y=self.cleaned_data[TARGET_VAR],
            mode='lines+markers', name='Original Data'
        ))
        # Plot the in-sample forecast
        fig.add_trace(go.Scatter(
            x=self.cleaned_data.index, y=self.cleaned_data[TARGET_VAR],
            mode='lines+markers', name='In-sample Forecast'
        ))
        # Plot the out-of-sample forecast
        future_dates = pd.date_range(start=self.cleaned_data.index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
        fig.add_trace(go.Scatter(
            x=future_dates, y=self.forecast_df['mean'],
            mode='lines+markers', name='Out-of-sample Forecast'
        ))
        # Plot the confidence intervals
        fig.add_trace(go.Scatter(
            x=future_dates, y=self.forecast_df['mean_ci_upper'],
            mode='lines', line=dict(width=0), showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=future_dates, y=self.forecast_df['mean_ci_lower'],
            mode='lines', fill='tonexty', line=dict(width=0),
            fillcolor='rgba(68, 68, 68, 0.1)', name='95% CI'
        ))
        fig.update_layout(
            title='ARIMA Model Forecast (Daily Data)',
            xaxis_title='Date (YYYY-MM)',
            yaxis_title=TARGET_VAR,
            template='plotly_white',
            width=800, height=400
        )
        fig.show()

if __name__ == '__main__':
    forecast_steps = 30
    original_data = pd.read_csv('data/women_bias_data.csv')
    Model(original_data.copy()).visualize(forecast_steps)
    data_unbiased = original_data.copy()[original_data['Bias'] == 1]
    Model(data_unbiased).visualize(forecast_steps)

