# ASSIGNMENT 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()
gap_2007 = gap[gap["year"] == 2007]

sns.set_theme(style="whitegrid")

# TASK 1
# Task 1: Ranked bar chart
# •	From gap_2007, select the 10 countries with the largest population using nlargest(10, "pop").
# •	Draw a horizontal bar chart with plt.barh(), showing population in millions (divide pop by 1,000,000). Sort the data so the largest bar is at the top.
# •	Which two countries are far ahead of the rest?


top10 = gap_2007.nlargest(10, "pop")
top10 = top10.sort_values("pop")

plt.figure(figsize=(10, 6))
plt.barh(top10["country"], top10["pop"] / 1000000)

plt.title("Top 10 Countries by Population (2007)")
plt.xlabel("Population (in millions)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

print("Answer: China and India are far ahead of the other countries.")



# TASK 2
# Task 2: Grouped bar chart
# •	Create a table of the average life expectancy of each continent for the years 1952 and 2007:
# g = gap[gap["year"].isin([1952, 2007])].groupby(["continent", "year"])["lifeExp"].mean().unstack()
# •	Draw it as a grouped bar chart using g.plot(kind="bar").
# •	Which continent improved the most between 1952 and 2007?


import plotly.express as px
import matplotlib.pyplot as plt

gap = px.data.gapminder()

g = gap[gap["year"].isin([1952, 2007])].groupby(
    ["continent", "year"]
)["lifeExp"].mean().unstack()

g.plot(kind="bar")
plt.ylabel("Average Life Expectancy")
plt.title("Life Expectancy by Continent")
plt.show()

print(g[2007] - g[1952])



# TASK 3
# Task 3: Change over time
# •	Select the data of India, China, Brazil and United States using gap[gap["country"].isin([...])].
# •	Draw a line chart of lifeExp against year, one line per country, using sns.lineplot(..., hue="country", marker="o").
# •	Which country started with the lowest life expectancy and which one improved the fastest? Why is a line chart the right choice here?


gap = px.data.gapminder()

countries = [ 
    "India",
    "China",
    "Brazil",
    "United States",
]
data = gap[gap["country"].isin(countries)]
plt.figure(figsize=(11, 6))
sns.lineplot(
    data=data, 
x="year",
 y="lifeExp",
  hue="country", 
  marker="o"
  )
plt.title("Life Expectancy Over Time")
plt.xlabel("Year")
plt.ylabel("Life Expectancy(years)")
plt.grid(True, alpha=0.3)
plt.legend(title="Country")
plt.show()



# TASK 4
# Task 4: Linear scale versus log scale
# •	Using gap_2007, draw two scatter plots side by side with gdpPercap on the x-axis and lifeExp on the y-axis.
# •	Keep the left chart as it is. On the right chart, add set_xscale("log").
# •	Which chart is easier to read, and why?


fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Linear scale
ax[0].scatter(gap_2007["gdpPercap"], gap_2007["lifeExp"])
ax[0].set_title("Linear Scale")
ax[0].set_xlabel("GDP per Capita (US dollars)")
ax[0].set_ylabel("Life Expectancy (years)")

# Logarithmic scale
ax[1].scatter(gap_2007["gdpPercap"], gap_2007["lifeExp"])
ax[1].set_xscale("log")
ax[1].set_title("Logarithmic Scale")
ax[1].set_xlabel("GDP per Capita (US dollars)")
ax[1].set_ylabel("Life Expectancy (years)")

plt.tight_layout()
plt.show()

print("Answer: The log-scale chart makes the relationship easier")
print("to see across countries with different income levels.")



# TASK 5
# Task 5: Bubble chart
# •	Draw an interactive chart where bubble size shows population and colour shows continent:
# fig = px.scatter(gap_2007, x="gdpPercap", y="lifeExp", size="pop", color="continent",
#                  hover_name="country", log_x=True, size_max=50)
# fig.show()
# •	Which continent has most of the countries with low life expectancy?
# •	Hover over the largest bubbles and write the names of two of them.


gap = px.data.gapminder()
gap_2007 = gap[gap["year"] == 2007]
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.scatterplot(
    data=gap_2007,
    x="gdpPercap",
    y="lifeExp",
    alpha=0.7,
    ax=axes[0]
)
fig = px.scatter(
    gap_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    title="Life Expectancy vs GDP per Capita",
)

fig.update_layout(
    xaxis_title="GDP per Capita",
    yaxis_title="Life Expectancy",
)

fig.show()



# TASK 6
# Task 6: Correlation heatmap
# •	Calculate the correlation matrix of lifeExp, pop and gdpPercap using .corr().
# •	Draw it with sns.heatmap(..., annot=True, cmap="coolwarm", vmin=-1, vmax=1).
# •	Which pair of columns is most strongly related? Which pair has almost no relationship?


gap = px.data.gapminder()
gap_2007 = gap[gap["year"] == 2007]
data = gap_2007[
    ["lifeExp","pop","gdpPercap"]
]
corr_matrix = data.corr()
print(corr_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot =True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt= ".2f"
)
plt.title("Correlation Heatmap(2007)")
plt.tight_layout()
plt.show()



# TASK 7
# Task 7: Pattern heatmap
# •	Create a table with continents as rows and years as columns showing average life expectancy:
# pivot = gap.pivot_table(index="continent", columns="year", values="lifeExp", aggfunc="mean")
# •	Draw it with sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu").
# •	Which continent has the lowest values throughout? In which years does the colour change fastest?


pivot = gap.pivot_table(
    index="continent",
    columns="year",
    values="lifeExp",
    aggfunc="mean"
)

plt.figure(figsize=(13, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Life Expectancy by Continent and Year")
plt.xlabel("Year")
plt.ylabel("Continent")

plt.tight_layout()
plt.show()

print("Answer: Africa generally has the lowest life expectancy.")



# TASK 8
# Task 8: Choose the right chart
# Copy this table into a Markdown cell. For each situation, choose the best chart (bar, line, scatter, histogram or heatmap) and give a one-line reason.


situations = [
    ("Compare students in five branches",
     "Bar chart",
     "Compares categories."),

    ("Show monthly temperature changes",
     "Line chart",
     "Shows changes over time."),

    ("Study hours versus marks",
     "Scatter plot",
     "Shows the relationship between two variables."),

    ("Marks distribution of 100 students",
     "Histogram",
     "Shows the distribution of numerical data."),

    ("Attendance of five subjects over six weeks",
     "Heatmap",
     "Shows patterns across subjects and weeks.")
]

for situation, chart, reason in situations:
    print("\nSituation:", situation)
    print("Best chart:", chart)
    print("Reason:", reason)



# TASK 9
# Run this code. It shows the life expectancy of the top 8 European countries, but the chart is badly designed.
# bad = gap_2007[gap_2007["continent"] == "Europe"].nlargest(8, "lifeExp")
# plt.figure(figsize=(6, 4))
# plt.bar(bad["country"], bad["lifeExp"],
#         color=["red", "green", "blue", "yellow", "pink", "orange", "purple", "black"])
# plt.ylim(79, 82)
# plt.show()
# •	List at least four problems with this chart.
# •	Redraw it properly: one colour, a y-axis (or x-axis) that starts at 0, readable country names, a title and axis labels.
# •	Write one line on how the bars look different after your fix.


bad = gap_2007[gap_2007["continent"] == "Europe"].nlargest(
    8, "lifeExp"
)

bad = bad.sort_values("lifeExp")

plt.figure(figsize=(10, 6))

plt.barh(bad["country"], bad["lifeExp"])

plt.title("Top 8 European Countries by Life Expectancy (2007)")
plt.xlabel("Life Expectancy (years)")
plt.ylabel("Country")
plt.xlim(0, 90)

plt.tight_layout()
plt.show()

print("Problems in the original chart:")
print("1. Too many different colours.")
print("2. The y-axis starts at 79 instead of zero.")
print("3. Country names may be difficult to read.")
print("4. The title is missing.")
print("5. Axis labels are missing.")

print("After correction, the chart is clearer and differences")
print("between countries are not exaggerated by a truncated axis.")


