# Data Analyst Master Toolkit 🐍📊

A reusable Python cheat sheet and analysis template for **Data Analysts**.

The goal of this repository is simple:

> **When I receive a dataset, I should not have to remember every Pandas/NumPy/Seaborn syntax from memory. I should be able to open this file, find the pattern I need, and continue my analysis.**

This repository focuses on practical **Python for Data Analysis**, not advanced Python programming.

---

## 🎯 What This Repository Covers

The toolkit follows a typical Data Analyst workflow:

```text
Dataset
   ↓
Load
   ↓
Understand
   ↓
Data Quality
   ↓
Clean
   ↓
Explore
   ↓
Group & Aggregate
   ↓
Filter
   ↓
Merge / Combine
   ↓
Calculate KPIs
   ↓
Analyze Trends
   ↓
Find Relationships
   ↓
Detect Outliers
   ↓
Visualize
   ↓
Generate Business Insights
```

---

# 📁 Repository Structure

```text
data-analyst-master-toolkit/
│
├── data_analyst_master_toolkit.py
└── README.md
```

---

# 🛠️ Requirements

Install the main Python libraries:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

`openpyxl` is required when working with Excel `.xlsx` files.

---

# 🚀 How to Use

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Put your dataset in the project folder

Example:

```text
data-analyst-master-toolkit/
│
├── data_analyst_master_toolkit.py
├── README.md
└── sales_data.csv
```

### 3. Change the dataset name

Open:

```text
data_analyst_master_toolkit.py
```

Change:

```python
DATA_FILE = "dataset.csv"
```

to:

```python
DATA_FILE = "sales_data.csv"
```

### 4. Run the file

```bash
python data_analyst_master_toolkit.py
```

---

# 📚 Sections Explained

## 1. Load Data

### CSV

```python
df = pd.read_csv("dataset.csv")
```

### Excel

```python
df = pd.read_excel("dataset.xlsx")
```

### When to use

Use this section whenever you receive a new dataset.

---

# 2. Dataset Understanding

Useful commands:

```python
df.shape
df.head()
df.tail()
df.columns
df.info()
df.describe()
```

### Questions answered

- How many rows are there?
- How many columns?
- What are the column names?
- What are the data types?
- What does the dataset look like?
- What are the basic statistics?

### Recommended approach

Always perform this step **before cleaning or analysis**.

---

# 3. Data Quality

## Missing values

```python
df.isnull().sum()
```

Percentage:

```python
df.isnull().mean() * 100
```

## Duplicate rows

```python
df.duplicated().sum()
```

## Unique values

```python
df["column"].unique()
```

## Frequency

```python
df["column"].value_counts()
```

### Questions answered

- Which columns contain missing data?
- How much data is missing?
- Are there duplicate records?
- How many categories exist?
- Are there suspicious/inconsistent values?

---

# 4. Data Cleaning

Common operations:

```python
df.dropna()
df.fillna()
df.drop_duplicates()
df.rename()
df.replace()
```

### Numerical missing values

A common option:

```python
df["sales"] = df["sales"].fillna(
    df["sales"].median()
)
```

### Categorical missing values

```python
df["region"] = df["region"].fillna(
    df["region"].mode()[0]
)
```

**Important:** Do not blindly fill every missing value. The correct treatment depends on the business meaning of the missing data.

---

# 5. Date Analysis

Convert dates:

```python
df["date"] = pd.to_datetime(df["date"])
```

Extract:

```python
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["quarter"] = df["date"].dt.quarter
df["weekday"] = df["date"].dt.day_name()
```

### Useful for

- Monthly sales
- Quarterly performance
- Year-over-year analysis
- Seasonality
- Weekday analysis

---

# 6. Numerical Analysis

Common statistics:

```python
df["sales"].mean()
df["sales"].median()
df["sales"].min()
df["sales"].max()
df["sales"].std()
```

Use:

```python
df.describe()
```

for a quick statistical overview.

---

# 7. Top and Bottom Performers

### Top 10

```python
df.nlargest(10, "sales")
```

### Bottom 10

```python
df.nsmallest(10, "sales")
```

### Sorting

```python
df.sort_values("sales", ascending=False)
```

### Typical business questions

- Top 10 products?
- Top 10 customers?
- Lowest-performing regions?
- Highest-profit transactions?

---

# 8. GroupBy ⭐

One of the most important Pandas operations for Data Analysts.

```python
df.groupby("category")["sales"].sum()
```

This answers:

> How much sales did each category generate?

### Multiple statistics

```python
df.groupby("category")["sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)
```

### Multiple metrics

```python
df.groupby("category").agg({
    "sales": "sum",
    "profit": "sum"
})
```

### Business thinking

Most business questions can be translated into:

```text
Dimension + Metric + Aggregation
```

Example:

```text
Region + Sales + Sum
```

becomes:

```python
df.groupby("region")["sales"].sum()
```

---

# 9. Filtering

### One condition

```python
df[df["sales"] > 10000]
```

### Multiple conditions

```python
df[
    (df["sales"] > 10000) &
    (df["region"] == "West")
]
```

### Multiple categories

```python
df[df["region"].isin(["West", "East"])]
```

### Range

```python
df[df["sales"].between(10000, 50000)]
```

Useful when investigating a particular segment or business condition.

---

# 10. Merge — Pandas JOIN

Pandas:

```python
orders.merge(
    customers,
    on="customer_id",
    how="left"
)
```

SQL equivalent:

```sql
SELECT *
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id;
```

### Join types

| Pandas | SQL |
|---|---|
| `how="inner"` | INNER JOIN |
| `how="left"` | LEFT JOIN |
| `how="right"` | RIGHT JOIN |
| `how="outer"` | FULL OUTER JOIN |

This is particularly useful when analysis requires combining multiple business datasets.

---

# 11. Concat

Use `concat()` when datasets need to be stacked.

```python
pd.concat([df1, df2], ignore_index=True)
```

Typical use case:

```text
January data
+
February data
+
March data
=
Q1 data
```

---

# 12. Calculated Columns

Create business metrics:

```python
df["profit_margin"] = (
    df["profit"] / df["sales"]
) * 100
```

Another example:

```python
df["revenue"] = (
    df["quantity"] * df["unit_price"]
)
```

Useful for creating:

- Revenue
- Profit
- Profit margin
- Conversion rate
- Average order value
- Growth rate
- Other business KPIs

---

# 13. Apply

Use `apply()` when you need custom logic.

Example:

```python
df["sales_category"] = df["sales"].apply(
    lambda x: "High" if x > 10000 else "Low"
)
```

### Important

Do not use `apply()` automatically for everything.

Prefer Pandas vectorized operations when possible because they are generally clearer and more efficient.

---

# 14. Correlation

Calculate:

```python
df.corr(numeric_only=True)
```

Visualize:

```python
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)
```

### Question answered

> Which numerical variables move together?

### Important

**Correlation does not prove causation.**

A strong correlation does not automatically mean one variable causes another.

---

# 15. Outlier Analysis

## Boxplot

```python
sns.boxplot(data=df, x="sales")
```

Useful for identifying unusually high or low observations.

## IQR method

```python
Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

Then:

```python
outliers = df[
    (df["sales"] < lower) |
    (df["sales"] > upper)
]
```

**Important:** An outlier is not automatically an error. Investigate it before removing it.

---

# 📊 Visualization Cheat Sheet

Choosing the correct chart is part of Data Analyst work.

| Business question | Recommended visualization |
|---|---|
| Compare sales by category | **Bar chart** |
| Compare regions | **Bar chart** |
| Top 10 products | **Horizontal bar chart** |
| Sales over time | **Line chart** |
| Monthly/quarterly trend | **Line chart** |
| Distribution of sales | **Histogram** |
| Distribution of age/income/etc. | **Histogram** |
| Identify outliers | **Boxplot** |
| Compare distributions across categories | **Boxplot** |
| Relationship between sales & profit | **Scatter plot** |
| Relationship between two numerical variables | **Scatter plot** |
| Correlation among many numerical variables | **Heatmap** |
| Frequency/count of categories | **Count plot** |
| Simple part-to-whole composition | **Pie chart** |
| Ranking many categories | **Horizontal bar chart** |

---

# 📊 1. Bar Chart

### Use when

You want to compare categories.

Example:

> Which region has the highest sales?

```python
sns.barplot(
    data=df,
    x="region",
    y="sales"
)
```

Best for:

- Region
- Category
- Department
- Product
- Segment

---

# 📊 2. Horizontal Bar Chart

### Use when

There are many categories or category names are long.

Example:

> Top 10 products by sales

```python
top10 = (
    df.groupby("product")["sales"]
    .sum()
    .nlargest(10)
    .sort_values()
)

top10.plot(kind="barh")
```

---

# 📈 3. Line Chart

### Use when

The x-axis represents time or another ordered sequence.

Example:

> How did sales change each month?

```python
sns.lineplot(
    data=df,
    x="date",
    y="sales"
)
```

Best for:

- Daily trends
- Monthly trends
- Quarterly trends
- Yearly trends
- Growth over time

---

# 📊 4. Histogram

### Use when

You want to understand the distribution of a numerical variable.

Example:

> How are order values distributed?

```python
sns.histplot(
    data=df,
    x="order_value",
    kde=True
)
```

Useful for:

- Age
- Salary
- Sales
- Order value
- Delivery time

---

# 📦 5. Boxplot

### Use when

You want to identify outliers or compare distributions.

```python
sns.boxplot(
    data=df,
    x="sales"
)
```

Also useful:

```python
sns.boxplot(
    data=df,
    x="region",
    y="sales"
)
```

---

# 🔵 6. Scatter Plot

### Use when

You want to investigate the relationship between two numerical variables.

Example:

> Is higher advertising spend associated with higher revenue?

```python
sns.scatterplot(
    data=df,
    x="ad_spend",
    y="revenue"
)
```

---

# 🔥 7. Heatmap

### Use when

You want to visualize a correlation matrix.

```python
correlation = df.corr(
    numeric_only=True
)

sns.heatmap(
    correlation,
    annot=True
)
```

Useful for:

- Correlation analysis
- Feature relationships
- Identifying potentially related variables

---

# 📊 8. Count Plot

### Use when

You want to count observations in each category.

```python
sns.countplot(
    data=df,
    x="category"
)
```

Example questions:

- How many customers are in each segment?
- How many orders come from each region?
- How many transactions belong to each status?

---

# 🥧 9. Pie Chart

Use **sparingly**.

Best when:

- There are only a few categories.
- Categories represent parts of one meaningful whole.

Example:

```python
df["category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
```

For many categories or precise comparisons, prefer a bar chart.

---

# 🧠 The Data Analyst Question Framework

When you receive a dataset, don't immediately start making charts.

Ask:

### 1. Understand

```text
What data do I have?
```

### 2. Validate

```text
Can I trust this data?
```

### 3. Describe

```text
What happened?
```

### 4. Compare

```text
Which category/region/product performed differently?
```

### 5. Diagnose

```text
Why might performance be high or low?
```

### 6. Trend

```text
How is performance changing over time?
```

### 7. Segment

```text
Which customer/product/region segments behave differently?
```

### 8. Investigate

```text
Are there anomalies or unusual observations?
```

### 9. Relate

```text
Which variables appear to be associated?
```

### 10. Recommend

```text
What action could the business consider?
```

---

# ⭐ The Universal Analysis Pattern

Most Data Analyst questions can be reduced to:

```text
BUSINESS QUESTION
       ↓
DIMENSION
       ↓
METRIC
       ↓
AGGREGATION
       ↓
FILTER / SORT
       ↓
VISUALIZATION
       ↓
INSIGHT
       ↓
BUSINESS ACTION
```

Example:

```text
Which region generates the most revenue?
       ↓
Dimension = Region
       ↓
Metric = Revenue
       ↓
Aggregation = SUM
       ↓
GROUPBY
       ↓
Sort descending
       ↓
Bar chart
       ↓
Identify leading/lagging regions
       ↓
Investigate why
```

---

# ⚡ Quick Reference

| Need | Pandas / Python |
|---|---|
| Dataset size | `df.shape` |
| First rows | `df.head()` |
| Columns | `df.columns` |
| Data types | `df.dtypes` |
| Full info | `df.info()` |
| Statistics | `df.describe()` |
| Missing values | `df.isnull().sum()` |
| Missing % | `df.isnull().mean() * 100` |
| Duplicates | `df.duplicated().sum()` |
| Unique values | `df["col"].unique()` |
| Unique count | `df["col"].nunique()` |
| Frequency | `df["col"].value_counts()` |
| Filter | `df[condition]` |
| Top N | `df.nlargest()` |
| Bottom N | `df.nsmallest()` |
| Sort | `df.sort_values()` |
| Group | `df.groupby()` |
| Join | `df.merge()` |
| Stack | `pd.concat()` |
| Create metric | `df["new"] = ...` |
| Dates | `pd.to_datetime()` |
| Correlation | `df.corr()` |
| Outliers | Boxplot / IQR |

---

# 📌 Important Principles

### Don't blindly delete missing values

Understand **why** they're missing.

### Don't blindly remove outliers

An outlier could be a data error — or a very important business event.

### Don't confuse correlation with causation

A relationship between two variables does not prove that one causes the other.

### Don't make charts just because you can

Every visualization should answer a question.

### Don't stop at "what happened"

A Data Analyst should try to move from:

```text
What happened?
       ↓
Why did it happen?
       ↓
What should we investigate/do next?
```

---

# 🎯 Goal of This Repository

This repository is **not designed to replace understanding**.

It is designed to solve a common practical problem:

> "I know what this Pandas/NumPy/Seaborn operation does, but I forgot the exact syntax."

Instead of searching Google every time, open this repository, find the relevant pattern, adapt the column names, and continue the analysis.

---

## Future Improvements

Potential future additions:

- Automated data profiling
- Automated KPI detection
- Automated visualization recommendations
- Statistical testing
- Advanced time-series analysis
- SQL-to-Pandas translation reference
- Excel-to-Pandas translation reference
- Business Analyst question templates
- Automated EDA report generation
- AI-powered insight generation

---

## Author

Created as a personal **Data Analyst reference toolkit** for practical analysis using Python, Pandas, NumPy, Matplotlib and Seaborn.
