


```markdown
# 📈 Predictive Analytics with Regression & ARIMA

This project demonstrates **predictive modeling and forecasting** using regression and ARIMA methods in Python.  
It uses a custom dataset (`future_forecast.csv`) containing forecast values and confidence intervals.

---

## 🚀 Features
- Load and preprocess historical forecast data
- Regression forecasting with evaluation metrics (R², RMSE, MAPE)
- ARIMA time-series forecasting with confidence intervals
- Visualization of predictions vs historical data
- Export of ARIMA forecast results to CSV

---

## 📂 Project Structure
```
PredictiveAnalytics/
│── data/
│   └── future_forecast.csv   # Input dataset
│── src/
│   └── forecast.py           # Main forecasting script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
```

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PredictiveAnalytics.git
   cd PredictiveAnalytics
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🐍 Usage

Run the forecasting script:

```bash
python src/forecast.py
```

This will:
- Print regression metrics (R², RMSE, MAPE)
- Generate regression and ARIMA forecast plots
- Save ARIMA forecast results to `data/arima_forecast_output.csv`

---

## 📊 Example Dataset

The dataset (`future_forecast.csv`) includes forecast values and confidence intervals:

```csv
date,forecast,lower_ci,upper_ci
2024-01-01,848.84,722.66,960.11
2024-01-02,807.37,689.21,927.70
2024-01-03,731.08,605.44,850.22
...
```

---

## 📈 Output

- **Regression Forecast:** Linear trend prediction with metrics (R², RMSE, MAPE).
- **ARIMA Forecast:** Next 10 days with confidence intervals.
- **Visualizations:** Forecast line with shaded confidence bands.
- **Export:** ARIMA forecast saved to `arima_forecast_output.csv`.

---

## 🛠 Troubleshooting
- If you see `ModuleNotFoundError`, install missing packages:
  ```bash
  pip install statsmodels pandas scikit-learn matplotlib
  ```
- Ensure IntelliJ’s Python interpreter matches the environment where dependencies are installed.

---

## 📜Athulya km
