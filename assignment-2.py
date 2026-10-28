# ASSIGNMENT 2



# TASK 1
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# sales = [12, 15, 14, 20, 24, 22]   # in thousands
# •	Draw a line chart of sales against months using plt.plot() with circle markers and a grid.
# •	Add a title, an x-axis label and a y-axis label.
# •	Which month had the highest sales?


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 20, 24, 22]

plt.plot(months, sales, marker="o", color="green")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()



# TASK 2
# •	Find the average tip for each day: avg_tip = tips.groupby("day")["tip"].mean().reindex(["Thur", "Fri", "Sat", "Sun"])
# •	Draw a bar chart using plt.bar() with a colour of your choice.
# •	On which day are tips the highest?


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 15000, 12000, 18000, 22000, 25000]

plt.bar(months, sales, color='green')

plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales (₹)')

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()



# TASK 3
# •	Create two charts in one figure using fig, axes = plt.subplots(1, 2, figsize=(12, 4)).
# •	On the left, draw a histogram of total_bill with 10 bins using axes[0].hist().
# •	On the right, draw a scatter plot of total_bill (x) against tip (y) using axes[1].scatter().
# •	Give each chart a title and axis labels using set_title(), set_xlabel() and set_ylabel().
# •	Save the figure with plt.savefig("tips_plots.png", dpi=150).
# •	In 2 lines, describe the most common bill range and the relationship between bill and tip.


tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(tips["total_bill"], bins=10, color="skyblue", edgecolor="black")
axes[0].set_title("Distribution of Total Bill")
axes[0].set_xlabel("Total Bill ($)")
axes[0].set_ylabel("Frequency")

axes[1].scatter(tips["total_bill"], tips["tip"], color="green")
axes[1].set_title("Total Bill vs Tip")
axes[1].set_xlabel("Total Bill ($)")
axes[1].set_ylabel("Tip ($)")

plt.tight_layout()

plt.savefig("tips_plots.png", dpi=150)

plt.show()



# TASK 4
# •	Draw sns.countplot(data=tips, x="day") to show the number of customers on each day.
# •	Draw sns.barplot(data=tips, x="day", y="total_bill") to show the average bill on each day.
# •	Which day has the most customers? Which day has the highest average bill?


tips = sns.load_dataset("tips")

# Create two charts in one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Count plot: Number of customers on each day
sns.countplot(data=tips, x="day", ax=axes[0], color="skyblue")
axes[0].set_title("Number of Customers by Day")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Number of Customers")

# Bar plot: Average bill on each day
sns.barplot(data=tips, x="day", y="total_bill", ax=axes[1], color="lightgreen")
axes[1].set_title("Average Bill by Day")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Average Total Bill ($)")

plt.tight_layout()
plt.show()

# Find the day with the most customers
customer_count = tips["day"].value_counts()
print("Day with the most customers:", customer_count.idxmax())

# Find the day with the highest average bill
avg_bill = tips.groupby("day")["total_bill"].mean()
print("Day with the highest average bill:", avg_bill.idxmax())
print("Highest average bill: $", round(avg_bill.max(), 2))



# TASK 5
# •	Draw sns.boxplot(data=tips, x="day", y="total_bill").
# •	Which day has the highest median bill? Are there dots beyond the whiskers? What do they represent?
# •	Redraw the plot with hue="sex" added and note one difference you see.



# TASK 6
# •	Draw sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", style="time").
# •	In one line, say whether smokers and non-smokers tip differently.



# TASK 7
# •	Draw sns.pairplot(iris, hue="species", vars=["sepal_length", "sepal_width", "petal_length", "petal_width"]).
# •	Which two measurements separate the three species best? Which species is the easiest to identify?



# TASK 8
# •	Create the chart and display it with fig.show():
# fig = px.scatter(tips, x="total_bill", y="tip", color="day", size="size",
#                  hover_data=["sex", "time"], title="Bill vs Tip")
# fig.show()
# •	Hover over points, zoom into an area, and click a day in the legend to hide it.
# •	Write two things you can do in this chart that you could not do in your Matplotlib charts.



# TASK 9
# •	Draw px.box(tips, x="day", y="total_bill", color="sex").
# •	Draw px.histogram(tips, x="total_bill", color="time", nbins=15).
# •	Which meal, Lunch or Dinner, has larger bills in general?



# TASK 10
# •	Draw px.line(stocks, x="date", y=["GOOG", "AAPL", "AMZN"]), then add fig.update_xaxes(rangeslider_visible=True).
# •	Which of the three stocks grew the most by the end of 2019?
# •	Use the slider to zoom into any three-month period and note what happened there.



# TASK 11
# Task 11: Copy this table into a Markdown cell and complete it based on what you experienced.


