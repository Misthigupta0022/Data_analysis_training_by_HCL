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

plt.figure(figsize=(10, 6))

for product in ["Laptops", "Phones", "Headphones"]:
    plt.plot(sales["North"], sales[product], marker="o", label=product)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales of Products in North Region")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("sales.png")
plt.show()