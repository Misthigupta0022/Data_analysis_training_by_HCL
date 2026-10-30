import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

region=["North", "South", "East", "West"]
plt.bar(region, [100, 150, 200, 250], color="blue")

sales_data = [10000, 10500, 200000, 25000]
plt.plot(region, sales_data, marker="o", color="green")
plt.title("Sales Data by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()