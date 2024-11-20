import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
import plotly.express as px
import plotly.graph_objects as go
from data_formatter import DataFormatter
from data_reader import DataReader
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

MAX_FORECAST_STEPS = 100


class Model:
    """Input data (could be complete or filtered) and output forecast_df."""
    training_data: pd.DataFrame
    forecast_df: pd.DataFrame | None

    def __init__(self, training_data: pd.DataFrame):
        """Only initialize self.data. forecast_df is left None.
        Assume that the user only wants prediction data for less than 100 days."""
        self.training_data = training_data
        self.forecast_df = None

    def predict(self):
        model = ARIMA(self.training_data, order=self._pdq())
        fitted_model = model.fit()
        print(fitted_model.summary())
        forecast = fitted_model.get_forecast(steps=MAX_FORECAST_STEPS)
        self.forecast_df = forecast.summary_frame(alpha=0.05)  # 95% confidence interval
        print(self.forecast_df[['mean', 'mean_ci_lower', 'mean_ci_upper']])
        return self

    def get_result(self, forecast_steps: int) -> pd.DataFrame:
        forecast_values = self.forecast_df['mean']
        future_dates = pd.date_range(start=self.training_data.index[-1] + pd.DateOffset(months=0), periods=forecast_steps+1, freq='D')
        forecast_values = forecast_values[forecast_values.index.isin(future_dates)]
        forecast_values = forecast_values.reset_index().rename(columns={'index': 'date'})

        # Concatenate the last entry of training_data to forecast_values.
        last_entry = self.training_data.iloc[-1]  # Series
        last_entry.name = pd.Timestamp(last_entry.name)
        last_entry = pd.DataFrame({'date': [last_entry.name], 'mean': [last_entry.iloc[0]]})
        forecast_values = (pd.concat([forecast_values, last_entry], ignore_index=True)
                           .sort_values(by='date').reset_index(drop=True))

        return forecast_values

    @staticmethod
    def _check_stationarity(data) -> int:
        d = 0
        data_diff = data
        while not Model._adf_test(data_diff) and d < 2:
            data_diff = data_diff.diff().dropna()
            d += 1
        return d

    @staticmethod
    def _adf_test(series) -> bool:
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

    @staticmethod
    def _determine_lag(values: np.ndarray) -> int:
        """Return the number of lags to be included in the ARIMA model.
        The point where ACF cuts off indicates the value of q, and the one for PACF indicates p."""
        for i in range(5):
            if float(values[i]) < 0:
                return max(i - 1, 1)
        return 4

    def _pdq(self) -> tuple[int, int, int]:
        """Return the p, d, q value of data."""
        # data = self.training_data
        # sample_size = len(data)
        # nlags = sample_size // 2
        # acf_values = acf(data, nlags)
        # pacf_values = pacf(data, nlags)
        # p = Model._determine_lag(pacf_values)
        # d = Model._check_stationarity(data)
        # q = Model._determine_lag(acf_values)
        # return (p, d, q)
        return (11, 2, 10)

    # Currently this method is only for internal use.
    def visualize(self, forecast_steps):
        """Visualize with Plotly."""
        TARGET_VAR = self.training_data.columns.tolist()[0]
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.training_data.index, y=self.training_data[TARGET_VAR],
            mode='lines+markers', name='Original Data'
        ))
        # Plot the in-sample forecast
        fig.add_trace(go.Scatter(
            x=self.training_data.index, y=self.training_data[TARGET_VAR],
            mode='lines+markers', name='In-sample Forecast'
        ))
        # Plot the out-of-sample forecast
        future_dates = pd.date_range(start=self.training_data.index[-1] + pd.DateOffset(months=0), periods=forecast_steps, freq='D')
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
    df = ((DataFormatter(DataReader("synthetic_data.csv").read_dataset())
           .filter_by("NoFilter","NoFilter")
           .filter_invalid_transactions()).get_frequency_data().get_data())
    df.set_index('date', inplace=True)
    all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
    df = df.reindex(all_dates, fill_value=0)
    df.index = df.index.date
    df.index.name = 'date'
    model = Model(df)
    model.predict().get_result(forecast_steps)
    model.visualize(forecast_steps)

    # Prediction accuracy test
    # Step 2: Define the range for A, B, and C
    date_A = df.index.min()
    date_C = df.index.max()
    date_B = date_A + (date_C - date_A) // 2  # Choose B as the midpoint between A and C

    # Step 3: Split the data
    train_data = df.loc[date_A:date_B]
    test_data = df.loc[date_B:date_C]

    # Step 4: Train the model on data between A and B
    model = Model(train_data)
    model.predict().get_result(forecast_steps)  # Trains the model internally

    # Step 5: Make predictions for dates between B and C
    predictions = model.predict().get_result(len(test_data) - 1)

    # Step 6: Extract the actual and predicted values for comparison
    actual = test_data["frequency"].values  # Replace "frequency" with the actual target column name
    predicted = predictions["mean"].values  # Replace "mean" with the column name for predictions

    # Step 7: Calculate Mean Squared Error (MSE)
    mse = mean_squared_error(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predicted)

    # Display results
    print(f"Evaluation Metrics for Predictions between {date_B} and {date_C}:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R²): {r2:.4f}")

