# Data Analyst Master Toolkit 🐍📊

A reusable Python cheat sheet for **Data Analysts**.

Use this repository as a quick reference whenever you receive a new dataset and forget the exact Pandas, NumPy, Matplotlib, or Seaborn syntax.

---

## 📁 Repository

```text
data-analyst-master-toolkit/
│
├── data_analyst_master_toolkit.py
└── README.md
```

---

## 🚀 Quick Start

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

Put your dataset in the same folder as the Python file and change:

```python
DATA_FILE = "dataset.csv"
```

to your dataset name.

For Excel:

```python
DATA_FILE = "dataset.xlsx"
```

---

# 🐍 Python Data Analyst Quick Reference

| What I need | Use this |
|---|---|
| Load CSV | `pd.read_csv("file.csv")` |
| Load Excel | `pd.read_excel("file.xlsx")` |
| Dataset size | `df.shape` |
| Number of rows | `df.shape[0]` |
| Number of columns | `df.shape[1]` |
| First rows | `df.head()` |
| Last rows | `df.tail()` |
| Column names | `df.columns` |
| Data types | `df.dtypes` |
| Full dataset information | `df.info()` |
| Numerical statistics | `df.describe()` |
| Categorical statistics | `df.describe(include="object")` |
| Missing values | `df.isnull().sum()` |
| Missing-value percentage | `df.isnull().mean() * 100` |
| Duplicate rows | `df.duplicated().sum()` |
| Remove duplicates | `df.drop_duplicates()` |
| Unique values | `df["column"].unique()` |
| Number of unique values | `df["column"].nunique()` |
| Category frequency | `df["column"].value_counts()` |
| Category percentage | `df["column"].value_counts(normalize=True) * 100` |
| Select one column | `df["column"]` |
| Select multiple columns | `df[["col1", "col2"]]` |
| Filter rows | `df[df["sales"] > 10000]` |
| Multiple AND conditions | `df[(condition1) & (condition2)]` |
| Multiple OR conditions | `df[(condition1) \| (condition2)]` |
| Filter from list | `df[df["region"].isin(["West", "East"])]` |
| Filter numeric range | `df[df["sales"].between(10000, 50000)]` |
| Sort descending | `df.sort_values("sales", ascending=False)` |
| Sort ascending | `df.sort_values("sales", ascending=True)` |
| Top N rows | `df.nlargest(10, "sales")` |
| Bottom N rows | `df.nsmallest(10, "sales")` |
| Mean | `df["sales"].mean()` |
| Median | `df["sales"].median()` |
| Minimum | `df["sales"].min()` |
| Maximum | `df["sales"].max()` |
| Standard deviation | `df["sales"].std()` |
| Group by + sum | `df.groupby("category")["sales"].sum()` |
| Group by + mean | `df.groupby("category")["sales"].mean()` |
| Group by + multiple statistics | `df.groupby("category")["sales"].agg(["sum", "mean", "min", "max", "count"])` |
| Group by + multiple metrics | `df.groupby("category").agg({"sales": "sum", "profit": "sum"})` |
| Group + sort | `df.groupby("category")["sales"].sum().sort_values(ascending=False)` |
| Create calculated column | `df["revenue"] = df["quantity"] * df["unit_price"]` |
| Profit margin | `df["profit_margin"] = (df["profit"] / df["sales"]) * 100` |
| Convert to datetime | `pd.to_datetime(df["date"])` |
| Extract year | `df["date"].dt.year` |
| Extract month | `df["date"].dt.month` |
| Extract quarter | `df["date"].dt.quarter` |
| Extract weekday | `df["date"].dt.day_name()` |
| Merge / JOIN datasets | `df1.merge(df2, on="id", how="left")` |
| Stack datasets | `pd.concat([df1, df2], ignore_index=True)` |
| Fill missing values | `df["column"].fillna(value)` |
| Fill with median | `df["column"].fillna(df["column"].median())` |
| Fill with mode | `df["column"].fillna(df["column"].mode()[0])` |
| Drop missing rows | `df.dropna()` |
| Rename columns | `df.rename(columns={"Old": "New"})` |
| Strip text whitespace | `df["column"].str.strip()` |
| Replace values | `df["column"].replace({"old": "new"})` |
| Correlation matrix | `df.corr(numeric_only=True)` |
| Custom logic | `df["column"].apply(function)` |
| IQR Q1 | `df["sales"].quantile(0.25)` |
| IQR Q3 | `df["sales"].quantile(0.75)` |
| Display DataFrame | `display(df)` |

---

# 📊 Visualization Quick Reference

| If I want to understand / show... | Use this visualization |
|---|---|
| Compare sales across categories | **Bar Chart** |
| Compare regions | **Bar Chart** |
| Compare departments | **Bar Chart** |
| Compare products | **Bar Chart** |
| Rank categories | **Bar Chart** |
| Top 10 products/customers | **Horizontal Bar Chart** |
| Many categories with long names | **Horizontal Bar Chart** |
| Sales over time | **Line Chart** |
| Revenue by month | **Line Chart** |
| Revenue by quarter | **Line Chart** |
| Yearly growth/trend | **Line Chart** |
| Distribution of sales | **Histogram** |
| Distribution of age | **Histogram** |
| Distribution of salary | **Histogram** |
| Distribution of order value | **Histogram** |
| Identify outliers | **Boxplot** |
| Compare distributions between categories | **Boxplot** |
| Sales vs Profit relationship | **Scatter Plot** |
| Revenue vs Advertising Spend | **Scatter Plot** |
| Relationship between two numerical variables | **Scatter Plot** |
| Correlation between many numerical variables | **Heatmap** |
| Frequency/count of categories | **Count Plot** |
| Number of customers by segment | **Count Plot** |
| Number of orders by status | **Count Plot** |
| Simple part-to-whole composition | **Pie Chart** |
| Percentage share with few categories | **Pie Chart** |

---

# 📌 Visualization Code Reference

### Bar Chart — Category Comparison

```python
sns.barplot(data=df, x="category", y="sales")
plt.show()
```

### Horizontal Bar — Ranking

```python
df.groupby("product")["sales"].sum().nlargest(10).sort_values().plot(
    kind="barh"
)
plt.show()
```

### Line Chart — Trend

```python
sns.lineplot(data=df, x="date", y="sales")
plt.show()
```

### Histogram — Distribution

```python
sns.histplot(data=df, x="sales", kde=True)
plt.show()
```

### Boxplot — Outliers

```python
sns.boxplot(data=df, x="sales")
plt.show()
```

### Scatter Plot — Relationship

```python
sns.scatterplot(data=df, x="sales", y="profit")
plt.show()
```

### Heatmap — Correlation

```python
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
```

### Count Plot — Frequency

```python
sns.countplot(data=df, x="category")
plt.show()
```

### Pie Chart — Part-to-Whole

```python
df["category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.show()
```

---

# ⚡ Business Question → Python Pattern

| Business question | Python pattern |
|---|---|
| Which category has the highest sales? | `df.groupby("category")["sales"].sum().sort_values(ascending=False)` |
| Which region has the highest revenue? | `df.groupby("region")["revenue"].sum().sort_values(ascending=False)` |
| Which product has the highest profit? | `df.groupby("product")["profit"].sum().sort_values(ascending=False)` |
| What are the top 10 products? | `df.nlargest(10, "sales")` |
| What are the bottom 10 products? | `df.nsmallest(10, "sales")` |
| What is the average order value? | `df["order_value"].mean()` |
| What is the median order value? | `df["order_value"].median()` |
| How many orders are there by status? | `df["status"].value_counts()` |
| How many customers are in each segment? | `df["segment"].value_counts()` |
| Which region has the highest average order value? | `df.groupby("region")["order_value"].mean().sort_values(ascending=False)` |
| Which delivery partner has the highest average delay? | `df.groupby("delivery_partner")["delay_minutes"].mean().sort_values(ascending=False)` |
| What is the monthly sales trend? | `df.groupby(df["date"].dt.to_period("M"))["sales"].sum()` |
| Which month had the highest sales? | `monthly_sales.sort_values(ascending=False).head(1)` |
| Are there missing values? | `df.isnull().sum()` |
| Are there duplicate records? | `df.duplicated().sum()` |
| Which variables are correlated? | `df.corr(numeric_only=True)` |
| Are there outliers? | `sns.boxplot(data=df, x="column")` |
| Combine two datasets | `df1.merge(df2, on="id", how="left")` |
| Calculate a new KPI | `df["new_metric"] = ...` |

---

# 🧠 Universal Data Analyst Workflow

```text
LOAD
  ↓
UNDERSTAND
  ↓
CHECK DATA QUALITY
  ↓
CLEAN
  ↓
DESCRIBE
  ↓
GROUP / FILTER
  ↓
CALCULATE KPIs
  ↓
ANALYZE TRENDS
  ↓
CHECK OUTLIERS
  ↓
CHECK RELATIONSHIPS
  ↓
VISUALIZE
  ↓
FIND BUSINESS INSIGHTS
```

---

## ⭐ Golden Rule

```text
Business Question
      ↓
Dimension
      ↓
Metric
      ↓
Aggregation
      ↓
Filter / Sort
      ↓
Visualization
      ↓
Insight
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
Bar Chart
      ↓
Business Insight
```

---

## 🎯 Repository Purpose

This repository is a **personal Data Analyst Python memory bank**.

The goal is not to memorize every Pandas or Seaborn command.

The goal is:

> **Know what you want to analyze → find the pattern → adapt the column names → analyze the data.**
