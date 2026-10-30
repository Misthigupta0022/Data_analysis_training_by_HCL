import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import display

sns.set_theme(style="whitegrid")

# Create Employee Dataset

details = pd.DataFrame({
    "Name": [
        "Anil", "Bala", "Charu", "Chitra", "Dinesh",
        "Dev", "Esha", "Fahad", "Gita", "Hari",
        "Isha", "Jatin", "Kiran", "Lata", "Mohan",
        "Nisha", "Omkar", "Pooja", "Qasim", "Rita",
        "Rahul", "Sahil", "Tina", "Unnati", "Usha",
        "Vani", "Vikram", "Waseem", "Xena", "Yash"
    ],

    "Age": [
        25, 30, 22, 28, 35, 27, 24, 29, 31, 26,
        23, 32, 34, 21, 33, 36, 28, 29, 30, 27,
        25, 31, 22, 24, 26, 28, 30, 32, 34, 29
    ],

    "Performance": [
        "Excellent", "Good", "Average", "Excellent", "Good",
        "Average", "Excellent", "Good", "Average", "Excellent",
        "Good", "Average", "Excellent", "Good", "Average",
        "Excellent", "Good", "Average", "Excellent", "Good",
        "Average", "Excellent", "Good", "Average", "Excellent",
        "Good", "Average", "Excellent", "Good", "Average"
    ],

    "Job Station": [
        "Bangalore", "Kolkata", "Mumbai", "Pune", "New Delhi",
        "Chennai", "Hyderabad", "Mumbai", "Noida", "Bangalore",
        "Kolkata", "New Delhi", "Pune", "Chennai", "Noida",
        "Hyderabad", "Mumbai", "Bangalore", "Chennai", "Pune",
        "New Delhi", "Noida", "Kolkata", "Hyderabad", "Mumbai",
        "Pune", "Chennai", "Bangalore", "Noida", "New Delhi"
    ],

    "Skills": [
        "Python", "SQL", "Java", "Excel", "Machine Learning",
        "C++", "Web Development", "Data Analysis", "Excel",
        "Communication", "SQL", "Python", "C++", "Java",
        "Data Analysis", "Machine Learning", "Web Development",
        "Excel", "Python", "Communication", "Java",
        "SQL", "Machine Learning", "C++", "Data Analysis",
        "Web Development", "Python", "Communication", "Excel", "SQL"
    ],

    "Branch": [
        "ECE", "CSE", "IT", "ME", "CE",
        "CSE", "ECE", "ME", "IT", "CE",
        "ME", "IT", "CSE", "ECE", "CE",
        "IT", "ME", "CSE", "ECE", "IT",
        "CE", "ECE", "ME", "IT", "CSE",
        "ECE", "CE", "CSE", "ME", "IT"
    ],

    "Annual Package": [
        50000, 60000, 55000, 65000, 70000,
        52000, 58000, 62000, 68000, 72000,
        54000, 64000, 0, 56000, 74000,
        58000, 68000, 75000, 62000, 71000,
        0, 67000, 59000, 63000, 76000,
        57000, 69000, 0, 61000, 73000
    ]
})

# Display Dataset

print("Total Employee Records:", len(details))
display(details.head(10))

# Display All Records
display(details)

# Display Column Names
print("Columns:", details.columns.tolist())

# Check Data Types
print("\nData Types:")
print(details.dtypes)

# Check Missing Values
print("\nMissing Values:")
print(details.isnull().sum())

# Basic Numerical Summary
display(details.describe())


# Fetch Employee Details by Name

name = input("Enter employee name: ")

result = details[
    details["Name"].str.lower() == name.lower()
]

if not result.empty:
    display(result)
else:
    print("Employee not found!")


# Fetch Names of IT Branch

it_students = details.loc[
    details["Branch"] == "IT",
    ["Name"]
]

display(it_students)

print("Total IT Employees:", len(it_students))


# Fetch Name and Age of CSE and ECE Branch

cse_students = details.loc[
    details["Branch"] == "CSE",
    ["Name", "Age"]
]

ece_students = details.loc[
    details["Branch"] == "ECE",
    ["Name", "Age"]
]

display(cse_students)
display(ece_students)


# Convert Performance into Numerical Score

performance_score = {
    "Average": 1,
    "Good": 2,
    "Excellent": 3
}

details["Performance Score"] = (
    details["Performance"].map(performance_score)
)


# Find Top Performers in Each Branch

top_score = (
    details.groupby("Branch")["Performance Score"]
    .transform("max")
)

top_performers = details[
    details["Performance Score"] == top_score
]

display(
    top_performers[
        ["Branch", "Name", "Performance", "Performance Score"]
    ].sort_values("Branch")
)


# Average Performance by Branch

average_performance = (
    details.groupby("Branch")
    .agg(
        Average_Performance=("Performance Score", "mean"),
        Employee_Count=("Name", "count")
    )
    .round(2)
    .reset_index()
)

display(average_performance)


# Top 10 Performers by Branch

top_10_performers = (
    details.sort_values(
        ["Branch", "Performance Score", "Annual Package"],
        ascending=[True, False, False]
    )
    .groupby("Branch")
    .head(10)
)

display(
    top_10_performers[
        ["Branch", "Name", "Performance",
         "Performance Score", "Annual Package"]
    ].reset_index(drop=True)
)


# Employee Count by Branch

branch_count = (
    details["Branch"]
    .value_counts()
    .reset_index()
)

branch_count.columns = ["Branch", "Count"]

display(branch_count)


# Employee Percentage by Branch

branch_percentage = (
    details["Branch"].value_counts(normalize=True) * 100
).round(2)

display(branch_percentage.rename("Percentage").to_frame())


# Annual Package Summary by Branch

package_summary = (
    details.groupby("Branch")["Annual Package"]
    .agg(
        Highest_Package="max",
        Average_Package="mean",
        Lowest_Package="min"
    )
    .round(2)
    .reset_index()
)

display(package_summary)


# Visualization 1: Employee Count by Branch

plt.figure(figsize=(8, 5))

sns.countplot(
    data=details,
    x="Branch",
    order=sorted(details["Branch"].unique())
)

plt.title("Employee Count by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()


# Visualization 2: Average Performance by Branch

plt.figure(figsize=(8, 5))

sns.barplot(
    data=average_performance,
    x="Branch",
    y="Average_Performance"
)

plt.title("Average Performance by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Performance Score")
plt.ylim(0, 3)
plt.tight_layout()
plt.show()


# Visualization 3: Annual Package by Branch

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=details,
    x="Branch",
    y="Annual Package"
)

plt.title("Annual Package by Branch")
plt.xlabel("Branch")
plt.ylabel("Annual Package")
plt.tight_layout()
plt.show()


# Visualization 4: Performance Categories by Branch

plt.figure(figsize=(9, 5))

sns.countplot(
    data=details,
    x="Branch",
    hue="Performance",
    hue_order=["Average", "Good", "Excellent"]
)

plt.title("Performance Categories by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Employees")
plt.legend(title="Performance")
plt.tight_layout()
plt.show()


# Visualization 5: Annual Package Distribution

plt.figure(figsize=(8, 5))

plt.hist(
    details["Annual Package"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Annual Packages")
plt.xlabel("Annual Package")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()


# Employee Data Analytics Report

branch_count = details["Branch"].value_counts()

average_scores = (
    details.groupby("Branch")["Performance Score"].mean()
)

package_by_branch = (
    details.groupby("Branch")["Annual Package"]
    .agg(["max", "mean", "min"])
)

print("\nEMPLOYEE DATA ANALYTICS REPORT")
print("=" * 40)

print(
    "Largest Branch:",
    branch_count.idxmax(),
    "-", branch_count.max(), "employees"
)

print(
    "Highest Average Performance:",
    average_scores.idxmax(),
    "-", round(average_scores.max(), 2)
)

print(
    "Branch with Highest Maximum Package:",
    package_by_branch["max"].idxmax(),
    "-", package_by_branch["max"].max()
)

print(
    "Branch with Lowest Minimum Package:",
    package_by_branch["min"].idxmin(),
    "-", package_by_branch["min"].min()
)

print("\nNote: Results are based on the given employee dataset.")


# Export Data into CSV Files

details.to_csv("employee_dataset.csv", index=False)

average_performance.to_csv(
    "average_performance.csv", index=False
)

top_10_performers.to_csv(
    "top_10_performers.csv", index=False
)

package_summary.to_csv(
    "package_summary.csv", index=False
)

branch_count.to_csv(
    "branch_count.csv", index=False
)

print("\nAll CSV files exported successfully.")


# Read CSV File

df = pd.read_csv("employee_dataset.csv")

display(df.head())

print("Shape:", df.shape)

print("Columns:", df.columns)