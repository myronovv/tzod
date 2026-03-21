import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=200, freq="D")
true_values = 100 + np.sin(np.linspace(0, 10, 200)) * 20 + np.random.normal(0, 3, 200)

df = pd.DataFrame({
    "date": dates,
    "consumption": true_values
})

df.set_index("date", inplace=True)

df_missing = df.copy()
missing_idx = np.random.choice(df.index, size=40, replace=False)
df_missing.loc[missing_idx, "consumption"] = np.nan

df_linear = df_missing.copy()
df_linear["consumption"] = df_linear["consumption"].interpolate(method="linear")

df_poly = df_missing.copy()
df_poly["consumption"] = df_poly["consumption"].interpolate(method="polynomial", order=2)

df_spline = df_missing.copy()
df_spline["consumption"] = df_spline["consumption"].interpolate(method="spline", order=2)

mask = df_missing["consumption"].isna()

mse_linear = mean_squared_error(df.loc[mask, "consumption"], df_linear.loc[mask, "consumption"])
mse_poly = mean_squared_error(df.loc[mask, "consumption"], df_poly.loc[mask, "consumption"])
mse_spline = mean_squared_error(df.loc[mask, "consumption"], df_spline.loc[mask, "consumption"])

print("Похибки (MSE):")
print(f"Лінійна інтерполяція:   {mse_linear:.2f}")
print(f"Поліноміальна:          {mse_poly:.2f}")
print(f"Сплайн:                 {mse_spline:.2f}")

plt.figure()
plt.plot(df.index, df["consumption"], label="True", linewidth=2)
plt.plot(df_missing.index, df_missing["consumption"], "o", label="Missing", alpha=0.5)
plt.plot(df_linear.index, df_linear["consumption"], label="Linear")
plt.plot(df_poly.index, df_poly["consumption"], label="Polynomial")
plt.plot(df_spline.index, df_spline["consumption"], label="Spline")

plt.title("Інтерполяція енергоспоживання")
plt.legend()
plt.show()

methods = ["Linear", "Polynomial", "Spline"]
errors = [mse_linear, mse_poly, mse_spline]

plt.figure()
plt.bar(methods, errors)
plt.title("Порівняння похибок (MSE)")
plt.xlabel("Метод")
plt.ylabel("Помилка")
plt.show()