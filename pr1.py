import pandas as pd

data = {
    "product": [
        "Apple", "Banana", "Milk", "Bread", "Apple",
        "Milk", "Cheese", "Banana", "Juice", "Bread",
        "Apple", "Tea", "Coffee", "Milk", "Juice",
        "Cheese", "Tea", "Banana", "Coffee", "Yogurt"
    ],
    "total": [
        120, 80, 150, 60, 130,
        170, 200, 90, 140, 70,
        110, 95, 180, 160, 150,
        210, 100, 85, 190, 75
    ]
}

df = pd.DataFrame(data)

agg_df = (
    df.groupby("product")["total"]
    .agg(["count", "sum", "mean", "median", "std"])
    .reset_index()
)

agg_df = agg_df.sort_values(by="sum", ascending=False).reset_index(drop=True)

total_revenue = agg_df["sum"].sum()
agg_df["share"] = agg_df["sum"] / total_revenue * 100

top5 = agg_df.head(5).copy()
others = agg_df.iloc[5:].copy()

if not others.empty:
    others_row = pd.DataFrame({
        "product": ["Інші"],
        "count": [others["count"].sum()],
        "sum": [others["sum"].sum()],
        "mean": [others["sum"].sum() / others["count"].sum()],
        "median": [None],
        "std": [None],
        "share": [others["sum"].sum() / total_revenue * 100]
    })

    final_df = pd.concat([top5, others_row], ignore_index=True)
else:
    final_df = top5.copy()

final_df["mean"] = final_df["mean"].round(2)
final_df["median"] = final_df["median"].round(2)
final_df["std"] = final_df["std"].round(2)
final_df["share"] = final_df["share"].round(2)

print("Результат: топ-5 товарів + Інші")
print(final_df.to_string(index=False))