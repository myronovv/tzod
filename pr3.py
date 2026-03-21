import pandas as pd
import numpy as np

n = 100000

df = pd.DataFrame({
    "region": np.random.choice(["North", "South", "East", "West"], size=n),
    "energy_type": np.random.choice(["Solar", "Wind", "Hydro", "Gas"], size=n),
    "consumption_mwh": np.random.randint(100, 5000, size=n),
    "production_mwh": np.random.randint(100, 5000, size=n),
    "loss_percent": np.random.uniform(0, 20, size=n),
    "year": np.random.randint(2018, 2026, size=n)
})

memory_before = df.memory_usage(deep=True).sum() / 1024**2

print("Використання пам'яті ДО оптимізації:")
print(df.dtypes)
print(f"\nЗагальна пам'ять: {memory_before:.2f} MB")

df_optimized = df.copy()

df_optimized["region"] = df_optimized["region"].astype("category")
df_optimized["energy_type"] = df_optimized["energy_type"].astype("category")
df_optimized["consumption_mwh"] = df_optimized["consumption_mwh"].astype("int16")
df_optimized["production_mwh"] = df_optimized["production_mwh"].astype("int16")
df_optimized["loss_percent"] = df_optimized["loss_percent"].astype("float32")
df_optimized["year"] = df_optimized["year"].astype("int16")

memory_after = df_optimized.memory_usage(deep=True).sum() / 1024**2

print("\n" + "=" * 50)
print("Використання пам'яті ПІСЛЯ оптимізації:")
print(df_optimized.dtypes)
print(f"\nЗагальна пам'ять: {memory_after:.2f} MB")

saved_mb = memory_before - memory_after
saved_percent = (saved_mb / memory_before) * 100

print("\n" + "=" * 50)
print("ПОРІВНЯННЯ:")
print(f"Пам'ять до оптимізації:    {memory_before:.2f} MB")
print(f"Пам'ять після оптимізації: {memory_after:.2f} MB")
print(f"Зекономлено:              {saved_mb:.2f} MB")
print(f"Економія:                 {saved_percent:.2f}%")