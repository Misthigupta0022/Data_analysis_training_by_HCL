import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from io import StringIO

# Reproducibility
np.random.seed(7)

# Create date range
dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")

cities = ["Delhi", "Mumbai", "Bengaluru"]
categories = ["Electronics", "Clothing", "Grocery"]

# Create DataFrame
df = pd.DataFrame(
    [(d, c, k) for d in dates for c in cities for k in categories],
    columns=["Date", "City", "Category"]
)

# Base revenue
base = {
    "Electronics": 400,
    "Clothing": 250,
    "Grocery": 150
}

n = len(df)

# Random discounts
df["Discount"] = np.random.choice([0, 5, 10, 15, 20], n)

# Factors
trend = 1 + df["Date"].dt.dayofyear / 365 * 0.3

weekend = np.where(df["Date"].dt.dayofweek >= 5, 1.25, 1.0)

festive = np.where(df["Date"].dt.month.isin([10, 11]), 1.3, 1.0)

city_factor = df["City"].map({
    "Delhi": 1.0,
    "Mumbai": 1.15,
    "Bengaluru": 0.9
})

# Revenue calculation
df["Revenue"] = (
    df["Category"].map(base)
    * trend
    * weekend
    * festive
    * city_factor
    * (1 + df["Discount"] / 100)
    * np.random.normal(1, 0.08, n)
).round(1)

# Add outliers
df.loc[[100, 1502, 2801], "Revenue"] *= 8

print(df)





#Task-1
# ===========================
# Task-1 : Data Exploration
# ===========================

import streamlit as st
from io import StringIO

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------
st.title("📊 Retail Sales Dashboard")
st.subheader("Assignment 5 - Part A : Task 1")
st.write("Visual Exploration of Retail Sales Data - 2025")

# -----------------------------------
# Dataset Preview
# -----------------------------------
st.header("1. Original Sales Dataset")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# -----------------------------------
# Dataset Information
# -----------------------------------
st.header("2. Dataset Information - df.info()")

buffer = StringIO()
df.info(buf=buffer)

st.code(
    buffer.getvalue(),
    language="text"
)

# -----------------------------------
# Descriptive Statistics
# -----------------------------------
st.header("3. Descriptive Statistics")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

# -----------------------------------
# Missing Values
# -----------------------------------
st.header("4. Missing Values")

missing = df.isnull().sum()

st.dataframe(
    missing.reset_index().rename(
        columns={
            "index": "Column",
            0: "Missing Values"
        }
    ),
    use_container_width=True
)

# -----------------------------------
# Create Month & Weekday Columns
# -----------------------------------
st.header("5. Create Monthly and Weekly Columns")

df["Month"] = df["Date"].dt.month
df["Weekday"] = df["Date"].dt.day_name()

st.dataframe(
    df.head(10),
    use_container_width=True
)

# -----------------------------------
# Dataset Summary
# -----------------------------------
# -----------------------------------
# Dataset Summary
# -----------------------------------
st.header("6. Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Rows",
        len(df)
    )

with col2:
    st.metric(
        "Total Cities",
        df["City"].nunique()
    )

with col3:
    st.metric(
        "Total Categories",
        df["Category"].nunique()
    )

with col4:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

# -----------------------------------
# Date Range
# -----------------------------------
st.header("7. Date Range")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Start Date",
        df["Date"].min().strftime("%Y-%m-%d")
    )

with col2:
    st.metric(
        "End Date",
        df["Date"].max().strftime("%Y-%m-%d")
    )
# -----------------------------------
# Observations
# -----------------------------------
st.header("8. Observations")

st.write("Total Rows:", len(df))

st.write(
    "Total Columns after adding Month and Weekday:",
    len(df.columns)
)

st.write(
    "Date Range: 01 January 2025 to 31 December 2025"
)

st.write(
    "Missing Values:",
    int(df.isnull().sum().sum())
)

st.info(
    """
    ✅ Month contains values from 1 to 12

    ✅ Weekday contains names from Monday to Sunday

    ✅ No missing values found in the dataset

    ✅ Dataset contains sales data for 3 cities

    ✅ Dataset contains 3 product categories

    ✅ Revenue includes seasonal, weekend, discount,
       city and trend effects

    ✅ Three artificial outliers were added for analysis
    """
)

# -----------------------------------
# Revenue by City
# -----------------------------------
st.header("9. Revenue by City")

city_summary = (
    df.groupby("City")["Revenue"]
    .sum()
    .reset_index()
)

st.dataframe(
    city_summary,
    use_container_width=True
)

# Optional: City Revenue Chart
fig = px.bar(
    city_summary,
    x="City",
    y="Revenue",
    color="City",
    title="Total Revenue by City",
    text_auto=".2s"
)

st.plotly_chart(
    fig,
    use_container_width=True
)





#Task-2
n=len(df)
df["Discount"] = np.random.choice([0, 5, 10, 15, 20], size=n)