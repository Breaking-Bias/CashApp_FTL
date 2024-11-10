import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA, ARIMAResults
from statsmodels.tsa.stattools import adfuller, acf, pacf
import plotly.express as px
import plotly.graph_objects as go

MAX_FORECAST_STEPS = 100


class Model:
    """Input data (could be complete or filtered) and output forecast_df."""
    data: pd.DataFrame
    forecast_df: pd.DataFrame | None

    def __init__(self, data: pd.DataFrame):
        """Only initialize self.data. forecast_df is left None.
        Assume that the user only wants prediction data for less than 100 days."""
        self.data = data
        # self.data.set_index('date', inplace=True)
        self.forecast_df = None

    def predict(self):
        model = ARIMA(self.data, order=self._pdq())
        fitted_model = model.fit()
        print(fitted_model.summary())
        forecast = fitted_model.get_forecast(steps=MAX_FORECAST_STEPS)
        self.forecast_df = forecast.summary_frame(alpha=0.05)  # 95% confidence interval
        print(self.forecast_df[['mean', 'mean_ci_lower', 'mean_ci_upper']])
        return self

    def get_result(self, forecast_steps: int) -> pd.DataFrame:
        forecast_values = self.forecast_df['mean']
        future_dates = pd.date_range(start=self.data.index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
        return forecast_values[forecast_values.index.isin(future_dates)]

    def _check_stationarity(self, data) -> int:
        d = 0
        data_diff = data
        while not self._adf_test(data_diff) and d < 2:
            data_diff = data_diff.diff().dropna()
            d += 1
        return d

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

    def _pdq(self) -> tuple[int, int, int]:
        """Return the p, d, q value of data."""
        # sample_size = len(data)
        # nlags = sample_size // 2
        # acf_values = acf(data, nlags)
        # pacf_values = pacf(data, nlags)
        # p = self._determine_lag(pacf_values)
        # d = self._check_stationarity(data)
        # q = self._determine_lag(acf_values)
        # return (p, d, q)
        return (10, 2, 10)

    # Currently this method is only for internal use.
    def visualize(self, forecast_steps):
        """Visualize with Plotly."""
        TARGET_VAR = self.data.columns.tolist()[0]
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.data.index, y=self.data[TARGET_VAR],
            mode='lines+markers', name='Original Data'
        ))
        # Plot the in-sample forecast
        fig.add_trace(go.Scatter(
            x=self.data.index, y=self.data[TARGET_VAR],
            mode='lines+markers', name='In-sample Forecast'
        ))
        # Plot the out-of-sample forecast
        future_dates = pd.date_range(start=self.data.index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
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

