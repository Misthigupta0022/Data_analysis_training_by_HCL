import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from IPython.display import display, Image

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Laptops": [40, 42, 45, 38, 36, 35, 41, 48, 52, 85, 95, 60],
    "Phones": [55, 54, 58, 60, 57, 59, 62, 64, 66, 90, 98, 72],
    "Headphones": [20, 22, 21, 25, 23, 24, 26, 27, 30, 45, 52, 40]
})

display(sales)

colors = {
    "Laptops": "#0072B2",
    "Phones": "#D55E00",
    "Headphones": "#009E73"
}

fig, ax = plt.subplots(figsize=(13, 7))

for product in colors:
    ax.plot(sales["Month"], sales[product], color=colors[product], linewidth=2.5, marker='o')
    ax.text(11.2, sales[product].iloc[-1], product, color=colors[product], fontsize=11, va="center")

ax.set_title("Phones lead all year, and every product peaks in November", fontsize=14, fontweight="bold", loc="left")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (Rs. thousands)")

ax.axvspan(8.5, 10.5, color="orange", alpha=0.2)

ax.annotate("Festive Season Peak", xy=(10, 98), xytext=(5.5, 90), arrowprops=dict(arrowstyle='->'), fontsize=11)

ax.axhline(60, linestyle="--", color="grey", linewidth=1.5)

ax.text(0.2, 62, "Monthly Target", color="grey", fontsize=10)

ax.set_xlim(-0.5, 13)
ax.set_ylim(0, 115)

ax.spines[["top", "right"]].set_visible(False)

plt.savefig("after.png", dpi=150, bbox_inches="tight")

plt.show()