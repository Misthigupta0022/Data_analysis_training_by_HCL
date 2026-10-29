import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from IPython.display import display, Image

sales = pd.DataFrame({
    "North": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Laptops": [40, 42, 45, 30, 36, 35, 41, 48, 52, 85, 95, 60],
    "Phones": [55, 54, 58, 60, 57, 50, 62, 64, 66, 90, 98, 72],
    "Headphones": [20, 22, 25, 15, 18, 17, 30, 35, 40, 45, 50, 55]
})

display(sales)

colors = {
    "Laptops": "#C2185B",
    "Phones": "#F8C8DC",
    "Headphones": "#FF69B4"
}

fig, ax = plt.subplots(figsize=(12, 6))

for product in ["Laptops", "Phones", "Headphones"]:
    ax.plot(
        sales["North"],
        sales[product],
        marker="o",
        label=product,
        color=colors[product],
        linewidth=2.5
    )

    # Write product name at the end of each line
    ax.text(
        11.2,
        sales[product].iloc[-1],
        product,
        color=colors[product],
        fontsize=11,
        va="center"
    )

ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales in North Region")
ax.set_ylim(0, 110)
ax.set_xlim(-0.2, 13.5)
ax.legend()
ax.grid(True, alpha=0.3)

# Remove top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("sales.png", dpi=300)
plt.show()