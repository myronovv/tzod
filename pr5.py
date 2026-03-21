import pandas as pd
import numpy as np

data = {
    "consumption": [100, 120, np.nan, 140, np.nan, 160, 170, np.nan, 200]
}

df = pd.DataFrame(data)

print("Початкові дані:")
print(df)


def fill_mean(df, column):
    df_copy = df.copy()
    df_copy[column] = df_copy[column].fillna(df_copy[column].mean())
    return df_copy

def fill_median(df, column):
    df_copy = df.copy()
    df_copy[column] = df_copy[column].fillna(df_copy[column].median())
    return df_copy

def fill_forward(df, column):
    df_copy = df.copy()
    df_copy[column] = df_copy[column].fillna(method="ffill")
    return df_copy

def fill_backward(df, column):
    df_copy = df.copy()
    df_copy[column] = df_copy[column].fillna(method="bfill")
    return df_copy

df_mean = fill_mean(df, "consumption")
df_median = fill_median(df, "consumption")
df_ffill = fill_forward(df, "consumption")
df_bfill = fill_backward(df, "consumption")

print("\nЗаповнення середнім:")
print(df_mean)

print("\nЗаповнення медіаною:")
print(df_median)

print("\nЗаповнення попереднім значенням (ffill):")
print(df_ffill)

print("\nЗаповнення наступним значенням (bfill):")
print(df_bfill)