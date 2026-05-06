import pandas as pd
import matplotlib.pyplot as plt

files = {
    "LED": "led.csv",
    "Fluorescent": "fluorescent.csv",
    "Incandescent": "incandescent.csv"
}

results = {}

plt.figure()

for name, file in files.items():
    df = pd.read_csv(file)

    value_column = "BrightnessEV"

    if "timestamp" in df.columns:
        time_column = "timestamp"
    else:
        df["timestamp"] = range(len(df))
        time_column = "timestamp"

    avg = df[value_column].mean()
    results[name] = avg

    plt.plot(df[time_column], df[value_column], label=f"{name} (avg={avg:.2f})")

plt.xlabel("Time")
plt.ylabel("Brightness EV")
plt.title("Light Level Comparison")
plt.legend()
plt.grid()

plt.show()

print("Середні значення:")
for k, v in results.items():
    print(f"{k}: {v:.2f}")

plt.figure()
plt.bar(results.keys(), results.values())
plt.title("Average Brightness Comparison")
plt.ylabel("EV")
plt.grid(axis='y')

plt.show()