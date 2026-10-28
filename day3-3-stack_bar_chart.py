import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sales data
df = pd.DataFrame({
    "Month": ["January", "February", "March"],
    "North": [120, 135, 150],
    "South": [100, 110, 120],
    "East": [80, 95, 100],
    "West": [90, 100, 110]
})

# Line chart
plt.figure(figsize=(11, 6))

for region in ["North", "South", "East", "West"]:
    plt.plot(df["Month"], df[region], marker="o", label=region)

plt.title("Regional Sales Performance")
plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.legend()
plt.grid(alpha=0.3)

plt.show()