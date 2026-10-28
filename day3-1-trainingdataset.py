import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create the training dataset
np.random.seed(42)

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"],

    "North": [120, 135, 150, 160, 175, 190, 200, 210, 225, 240, 255, 270],
    "South": [100, 110, 125, 140, 150, 165, 175, 190, 205, 220, 230, 250],
    "East": [80, 95, 105, 120, 135, 145, 160, 175, 185, 200, 215, 230],
    "West": [90, 100, 115, 130, 140, 155, 170, 180, 195, 210, 225, 245],

    "Marketing_Spend": [20, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50],
    "Customers": [200, 240, 280, 310, 350, 390, 420, 460, 490, 530, 570, 610]
})

df["Total_Sales"] = df[["North", "South", "East", "West"]].sum(axis=1)
print(df)
df["Profit"] = (df["Total_Sales"] * 0.20).round(2)
print(df)
df["Profit"] = (df["Total_Sales"] * 0.20).round(2)
print(df)

# Calculate the sum of total profit
total_profit = df["Profit"].sum()
print("Total Profit:", round(total_profit, 2))
# Convert regional columns into rows
sales_data = df.melt(
    id_vars=["Month"],
    value_vars=["North", "South", "East", "West"],
    var_name="Region",
    value_name="Sales"
)

# Group by region and calculate sum and average
result = sales_data.groupby("Region")["Sales"].agg(
    ["sum", "mean"]
)

print(result)