import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load your CSV
# -------------------------------
df = pd.read_csv("../data/future_forecast.csv", parse_dates=["date"])

# -------------------------------
# Step 2: Inspect the data
# -------------------------------
print(df.head())

# Columns: date, forecast, lower_ci, upper_ci

# -------------------------------
# Step 3: Plot forecast with confidence intervals
# -------------------------------
plt.figure(figsize=(12,6))

plt.plot(df["date"], df["forecast"], label="Forecast", color="blue")
plt.fill_between(df["date"], df["lower_ci"], df["upper_ci"],
                 color="lightblue", alpha=0.4, label="Confidence Interval")

plt.title("Forecast with Confidence Intervals")
plt.xlabel("Date")
plt.ylabel("Forecast Value")
plt.legend()
plt.grid(True)
plt.show()
