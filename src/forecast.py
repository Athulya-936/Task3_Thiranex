import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import warnings

# Suppress noisy warnings
warnings.filterwarnings("ignore")

# -------------------------------
# Step 1: Load your dataset
# -------------------------------
data = pd.read_csv("../data/future_forecast.csv", parse_dates=["date"])
data.set_index("date", inplace=True)

# -------------------------------
# Utility: MAPE calculation
# -------------------------------
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# -------------------------------
# Step 2: Regression Forecasting
# -------------------------------
def regression_forecast(df):
    df['t'] = np.arange(len(df))  # time index
    X = df[['t']]
    y = df['forecast']

    model = LinearRegression()
    model.fit(X, y)

    # Predict next 10 steps
    future_t = np.arange(len(df), len(df)+10).reshape(-1,1)
    future_pred = model.predict(future_t)

    # Metrics
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = mse ** 0.5
    mape = mean_absolute_percentage_error(y, y_pred)

    print("Regression R²:", r2)
    print("Regression RMSE:", rmse)
    print("Regression MAPE:", mape)

    # Plot regression fit + forecast + CI
    plt.figure(figsize=(12,6))
    plt.plot(df.index, y, label="Forecast Data", color="blue")
    plt.plot(df.index, y_pred, label="Regression Fit", color="red")
    plt.plot(pd.date_range(df.index[-1], periods=10, freq="D"), future_pred,
             label="Future Forecast", color="green")
    plt.fill_between(df.index, df['lower_ci'], df['upper_ci'],
                     color="lightblue", alpha=0.4, label="Confidence Interval")
    plt.title("Regression Forecast with Confidence Interval")
    plt.legend()
    plt.grid(True)
    plt.show()

# -------------------------------
# Step 3: Time-Series Forecasting
# -------------------------------
def time_series_forecast(df):
    model = sm.tsa.ARIMA(df['forecast'], order=(2,1,2))  # ARIMA(p,d,q)
    results = model.fit()

    forecast_obj = results.get_forecast(steps=10)
    pred_mean = forecast_obj.predicted_mean
    conf_int = forecast_obj.conf_int()

    df_forecast = pd.DataFrame({
        "date": pred_mean.index,
        "forecast": pred_mean.values,
        "lower_ci": conf_int.iloc[:, 0].values,
        "upper_ci": conf_int.iloc[:, 1].values
    })

    print("ARIMA Forecasted values:")
    print(df_forecast)

    # Plot ARIMA forecast + CI
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['forecast'], label="Historical Forecast", color="blue")
    plt.plot(df_forecast["date"], df_forecast["forecast"], label="ARIMA Forecast", color="orange")
    plt.fill_between(df_forecast["date"], df_forecast["lower_ci"], df_forecast["upper_ci"],
                     color="lightblue", alpha=0.4, label="Confidence Interval")
    plt.title("ARIMA Forecast with Confidence Interval")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Save forecast to CSV
    df_forecast.to_csv("../data/arima_forecast_output.csv", index=False)

# -------------------------------
# Step 4: Run both methods
# -------------------------------
if __name__ == "__main__":
    regression_forecast(data)
    time_series_forecast(data)
