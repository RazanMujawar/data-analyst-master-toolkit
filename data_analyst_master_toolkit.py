"""
DATA ANALYST MASTER TOOLKIT
===========================

Reusable Python reference/template for exploratory data analysis (EDA).

How to use:
1. Put your CSV/XLSX file in the same folder.
2. Change DATA_FILE below.
3. Run the script.
4. Use the reference sections below when you need a specific analysis.

This is intentionally a "cheat code": it contains common Data Analyst
patterns rather than trying to automate every business decision.

Core stack:
    pandas
    numpy
    matplotlib
    seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================================
# 0. CONFIGURATION
# =============================================================================

DATA_FILE = "dataset.csv"

# For Excel:
# DATA_FILE = "dataset.xlsx"
# EXCEL_SHEET = "Sheet1"


# =============================================================================
# 1. LOAD DATA
# =============================================================================

# CSV
df = pd.read_csv(DATA_FILE)

# Excel examples:
# df = pd.read_excel(DATA_FILE)
# df = pd.read_excel(DATA_FILE, sheet_name=EXCEL_SHEET)

print("\n" + "=" * 70)
print("DATA LOADED")
print("=" * 70)


# =============================================================================
# 2. FIRST LOOK / DATASET UNDERSTANDING
# =============================================================================

print("\nShape:")
print(df.shape)

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nData types and non-null counts:")
df.info()

print("\nNumerical summary:")
print(df.describe())

print("\nCategorical summary:")
print(df.describe(include="object"))


# =============================================================================
# 3. DATA QUALITY CHECK
# =============================================================================

print("\n" + "=" * 70)
print("DATA QUALITY")
print("=" * 70)

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False))

print("\nMissing-value percentage:")
print(
    (df.isnull().mean() * 100)
    .sort_values(ascending=False)
)

print("\nDuplicate rows:")
print(df.duplicated().sum())

# To remove duplicates:
# df = df.drop_duplicates()


# =============================================================================
# 4. IDENTIFY COLUMN TYPES
# =============================================================================

num_cols = df.select_dtypes(include=np.number).columns.tolist()

cat_cols = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

date_cols = df.select_dtypes(
    include=["datetime64[ns]", "datetime64[ns, UTC]"]
).columns.tolist()

print("\nNumerical columns:")
print(num_cols)

print("\nCategorical columns:")
print(cat_cols)

print("\nDatetime columns:")
print(date_cols)


# =============================================================================
# 5. UNIQUE VALUES / FREQUENCIES
# =============================================================================

for col in cat_cols:
    print(f"\n{'-' * 60}")
    print(f"VALUE COUNTS: {col}")
    print("-" * 60)
    print(df[col].value_counts(dropna=False).head(10))

# Individual-column reference:
# df["column"].unique()
# df["column"].nunique()
# df["column"].value_counts()
# df["column"].value_counts(normalize=True) * 100


# =============================================================================
# 6. DATA CLEANING TOOLBOX
# =============================================================================

# Rename columns
# df.rename(columns={"Old Name": "new_name"}, inplace=True)

# Standardize column names
# df.columns = (
#     df.columns
#     .str.strip()
#     .str.lower()
#     .str.replace(" ", "_", regex=False)
# )

# Strip whitespace from text
# df["column"] = df["column"].str.strip()

# Replace values
# df["column"] = df["column"].replace({
#     "M": "Male",
#     "F": "Female"
# })

# Drop rows with missing values
# df = df.dropna()

# Drop a specific column
# df = df.drop(columns=["column"])

# Fill numerical missing values
# df["column"] = df["column"].fillna(df["column"].median())

# Fill categorical missing values
# df["column"] = df["column"].fillna(df["column"].mode()[0])

# Fill missing values with a fixed value
# df["column"] = df["column"].fillna(0)


# =============================================================================
# 7. DATE / TIME ANALYSIS
# =============================================================================

# Convert a column to datetime
# df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Extract date components
# df["year"] = df["date"].dt.year
# df["month"] = df["date"].dt.month
# df["quarter"] = df["date"].dt.quarter
# df["day"] = df["date"].dt.day
# df["weekday"] = df["date"].dt.day_name()

# Monthly aggregation
# monthly_sales = (
#     df.groupby(df["date"].dt.to_period("M"))["sales"]
#     .sum()
# )


# =============================================================================
# 8. NUMERICAL ANALYSIS
# =============================================================================

# Summary statistics
# df[num_cols].describe()

# Individual metrics
# df["sales"].mean()
# df["sales"].median()
# df["sales"].min()
# df["sales"].max()
# df["sales"].std()

# Quantiles
# df["sales"].quantile(0.25)
# df["sales"].quantile(0.50)
# df["sales"].quantile(0.75)


# =============================================================================
# 9. TOP / BOTTOM PERFORMERS
# =============================================================================

# Top 10
# df.nlargest(10, "sales")

# Bottom 10
# df.nsmallest(10, "sales")

# Sort descending
# df.sort_values("sales", ascending=False)

# Sort ascending
# df.sort_values("sales", ascending=True)


# =============================================================================
# 10. GROUPBY — MOST IMPORTANT DATA ANALYST PATTERN
# =============================================================================

# Total sales by category
# df.groupby("category")["sales"].sum()

# Multiple statistics
# df.groupby("category")["sales"].agg(
#     ["sum", "mean", "min", "max", "count"]
# )

# Multiple columns
# df.groupby("category").agg({
#     "sales": "sum",
#     "profit": "sum"
# })

# Sort a grouped result
# (
#     df.groupby("category")["sales"]
#     .sum()
#     .sort_values(ascending=False)
# )


# =============================================================================
# 11. BUSINESS QUESTION PATTERNS
# =============================================================================

# Which region has the highest sales?
# (
#     df.groupby("region")["sales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# Which product has the highest profit?
# (
#     df.groupby("product")["profit"]
#     .sum()
#     .sort_values(ascending=False)
# )

# Which delivery partner has the highest average delay?
# (
#     df.groupby("delivery_partner")["delay_minutes"]
#     .mean()
#     .sort_values(ascending=False)
# )

# Same idea for ANY dimension:
# df.groupby("DIMENSION")["METRIC"].AGGREGATION()


# =============================================================================
# 12. FILTERING
# =============================================================================

# One condition
# df[df["sales"] > 10000]

# Multiple AND conditions
# df[
#     (df["sales"] > 10000)
#     & (df["region"] == "West")
# ]

# Multiple OR conditions
# df[
#     (df["region"] == "West")
#     | (df["region"] == "East")
# ]

# Values in a list
# df[df["region"].isin(["West", "East"])]

# Numeric range
# df[df["sales"].between(10000, 50000)]

# Query syntax
# df.query("sales > 10000 and region == 'West'")


# =============================================================================
# 13. MERGE — PANDAS EQUIVALENT OF SQL JOIN
# =============================================================================

# Left join
# df = orders.merge(
#     customers,
#     on="customer_id",
#     how="left"
# )

# Inner join
# df = orders.merge(
#     customers,
#     on="customer_id",
#     how="inner"
# )

# Right join
# df = orders.merge(
#     customers,
#     on="customer_id",
#     how="right"
# )

# Outer join
# df = orders.merge(
#     customers,
#     on="customer_id",
#     how="outer"
# )


# =============================================================================
# 14. CONCAT — STACK DATASETS
# =============================================================================

# df = pd.concat([df1, df2], ignore_index=True)

# Multiple datasets:
# df = pd.concat([df1, df2, df3], ignore_index=True)


# =============================================================================
# 15. CALCULATED COLUMNS / BUSINESS METRICS
# =============================================================================

# Profit margin
# df["profit_margin"] = (df["profit"] / df["sales"]) * 100

# Revenue
# df["revenue"] = df["quantity"] * df["unit_price"]

# Percentage of total
# df["sales_share"] = (
#     df["sales"] / df["sales"].sum()
# ) * 100


# =============================================================================
# 16. APPLY / CUSTOM LOGIC
# =============================================================================

# Use apply when custom row/element-level logic is genuinely needed.
# Prefer vectorized Pandas operations when possible.

# Example:
# df["sales_category"] = df["sales"].apply(
#     lambda x: "High" if x > 10000 else "Low"
# )


# =============================================================================
# 17. CORRELATION
# =============================================================================

# Correlation matrix
# correlation = df.corr(numeric_only=True)
# print(correlation)

# Heatmap
# plt.figure(figsize=(10, 6))
# sns.heatmap(
#     correlation,
#     annot=True,
#     cmap="coolwarm",
#     fmt=".2f"
# )
# plt.title("Correlation Matrix")
# plt.show()

# Remember:
# Correlation does NOT prove causation.


# =============================================================================
# 18. OUTLIER ANALYSIS
# =============================================================================

# Boxplot
# plt.figure(figsize=(8, 4))
# sns.boxplot(data=df, x="sales")
# plt.title("Sales - Outlier Check")
# plt.show()

# IQR method
# Q1 = df["sales"].quantile(0.25)
# Q3 = df["sales"].quantile(0.75)
# IQR = Q3 - Q1
#
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
#
# outliers = df[
#     (df["sales"] < lower)
#     | (df["sales"] > upper)
# ]


# =============================================================================
# 19. TIME TREND ANALYSIS
# =============================================================================

# Monthly trend
# monthly_sales = (
#     df.groupby(df["date"].dt.to_period("M"))["sales"]
#     .sum()
# )
#
# monthly_sales.plot(kind="line", figsize=(10, 5))
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()


# =============================================================================
# 20. VISUALIZATION CHEAT SHEET
# =============================================================================

# ---------------------------------------------------------------------------
# A. BAR CHART — CATEGORY COMPARISON / RANKING
# ---------------------------------------------------------------------------

# Use when comparing categories, regions, products, departments, etc.

# sns.barplot(data=df, x="category", y="sales")
# plt.title("Sales by Category")
# plt.xticks(rotation=45)
# plt.show()


# ---------------------------------------------------------------------------
# B. HORIZONTAL BAR — MANY CATEGORIES / TOP-N
# ---------------------------------------------------------------------------

# Use when category names are long or there are many categories.

# top10 = (
#     df.groupby("product")["sales"]
#     .sum()
#     .nlargest(10)
#     .sort_values()
# )
#
# top10.plot(kind="barh", figsize=(8, 5))
# plt.title("Top 10 Products by Sales")
# plt.xlabel("Sales")
# plt.show()


# ---------------------------------------------------------------------------
# C. LINE CHART — TREND OVER TIME
# ---------------------------------------------------------------------------

# Use for daily/monthly/quarterly/yearly trends.

# sns.lineplot(data=df, x="date", y="sales")
# plt.title("Sales Trend")
# plt.show()


# ---------------------------------------------------------------------------
# D. HISTOGRAM — DISTRIBUTION OF ONE NUMERICAL VARIABLE
# ---------------------------------------------------------------------------

# Use to understand the shape/distribution of a numerical variable.

# sns.histplot(data=df, x="sales", kde=True)
# plt.title("Sales Distribution")
# plt.show()


# ---------------------------------------------------------------------------
# E. BOXPLOT — OUTLIERS + DISTRIBUTION
# ---------------------------------------------------------------------------

# Use to identify outliers and compare distributions.

# sns.boxplot(data=df, x="sales")
# plt.title("Sales Distribution and Outliers")
# plt.show()


# ---------------------------------------------------------------------------
# F. SCATTER PLOT — RELATIONSHIP BETWEEN TWO NUMERICAL VARIABLES
# ---------------------------------------------------------------------------

# Use for questions such as:
# Does advertising spend relate to revenue?
# Does sales relate to profit?

# sns.scatterplot(data=df, x="sales", y="profit")
# plt.title("Sales vs Profit")
# plt.show()


# ---------------------------------------------------------------------------
# G. HEATMAP — CORRELATION / MATRIX
# ---------------------------------------------------------------------------

# Use to inspect relationships between multiple numerical variables.

# correlation = df.corr(numeric_only=True)
# sns.heatmap(correlation, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()


# ---------------------------------------------------------------------------
# H. COUNT PLOT — FREQUENCY OF CATEGORIES
# ---------------------------------------------------------------------------

# Use when the question is:
# How many records/customers/orders belong to each category?

# sns.countplot(data=df, x="category")
# plt.title("Count by Category")
# plt.xticks(rotation=45)
# plt.show()


# ---------------------------------------------------------------------------
# I. PIE CHART — SIMPLE PART-TO-WHOLE
# ---------------------------------------------------------------------------

# Use sparingly. Best for a small number of categories that form a meaningful
# whole.

# counts = df["category"].value_counts()
# counts.plot(
#     kind="pie",
#     autopct="%1.1f%%",
#     figsize=(7, 7)
# )
# plt.title("Category Share")
# plt.ylabel("")
# plt.show()


# =============================================================================
# 21. COMMON DATA ANALYST QUESTIONS
# =============================================================================

"""
Whenever you receive a new dataset, ask:

1. How large is the dataset?
2. What does each column represent?
3. Which columns are numerical/categorical/date?
4. Are there missing values?
5. Are there duplicates?
6. Are there invalid or inconsistent values?
7. What are the key descriptive statistics?
8. What are the top performers?
9. What are the bottom performers?
10. How does the metric vary by category/region/product/customer?
11. What is the trend over time?
12. Are there outliers?
13. Which variables are correlated?
14. What segments behave differently?
15. Why is performance high or low?
16. What business problem does the data suggest?
17. What action could a business take?

Business-analysis thinking:

Overall KPI
    ↓
Dimension
    ↓
Segment
    ↓
Time
    ↓
Root cause
    ↓
Action
"""


# =============================================================================
# 22. QUICK REFERENCE — "WHAT DO I USE?"
# =============================================================================

"""
QUESTION / NEED                         USE

Dataset size                            df.shape
First look                              df.head()
Column names                            df.columns
Data types                              df.dtypes / df.info()
Statistics                              df.describe()
Missing values                          df.isnull().sum()
Duplicate rows                          df.duplicated().sum()
Unique categories                       df["col"].unique()
Category frequency                      df["col"].value_counts()
Filter rows                             df[condition]
Top N                                   df.nlargest()
Bottom N                                df.nsmallest()
Sort                                    df.sort_values()
Group + aggregate                       df.groupby()
Combine tables                          df.merge()
Stack datasets                          pd.concat()
Create metric                           df["new"] = ...
Dates                                   pd.to_datetime()
Time components                         .dt.year / .dt.month / ...
Correlation                             df.corr()
Outliers                                boxplot / IQR
Category comparison                     BAR CHART
Top-N ranking                           HORIZONTAL BAR
Time trend                              LINE CHART
Numerical distribution                  HISTOGRAM
Outliers                                BOXPLOT
Two numerical relationships             SCATTER PLOT
Correlation matrix                      HEATMAP
Category frequency                      COUNT PLOT
Simple part-to-whole                    PIE CHART (use sparingly)
"""


# =============================================================================
# END
# =============================================================================

print("\n" + "=" * 70)
print("MASTER TEMPLATE LOADED")
print("=" * 70)
print(
    "\nUse the commented sections as your Data Analyst Python reference."
)
