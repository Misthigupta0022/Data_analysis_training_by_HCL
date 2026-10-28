import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First bar chart
regions = ["North", "South", "East", "West"]
sales = [120, 100, 80, 90]

plt.figure(figsize=(9, 5))
plt.bar(regions, sales, color="steelblue")
plt.title("Sales Data by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.grid(axis="y")
plt.show()


# Grouped bar chart for three months
regions = ["North", "South", "East", "West"]

jan = [120, 100, 80, 90]
feb = [135, 110, 95, 100]
mar = [150, 120, 100, 110]

x = np.arange(len(regions))
width = 0.25

plt.figure(figsize=(10, 5))

plt.bar(x - width, jan, width=width, label="January")
plt.bar(x, feb, width=width, label="February")
plt.bar(x + width, mar, width=width, label="March")

plt.xticks(x, regions)
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.title("January vs February vs March Sales")
plt.legend()
plt.grid(axis="y")

plt.show()


plt.figure(figsize=(9, 5))
plt.bar(regions, jan, label="January")
plt.bar(regions, feb, bottom=jan, label="February")
plt.title("Combined sales by region")
plt.ylabel("Sales ($)")
plt.legend()
plt.show()