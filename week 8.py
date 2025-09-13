# =========================================
# Assignment: Analyzing Data with Pandas 
# and Visualizing Results with Matplotlib
# =========================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load the dataset
# ---------------------------
# Example: loading a CSV file (replace with your dataset)
df = pd.read_csv("data.csv")  

print("✅ Dataset Loaded Successfully!")
print("\nFirst 5 Rows of the Data:")
print(df.head())

# ---------------------------
# 2. Data Exploration
# ---------------------------
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------
# 3. Basic Analysis
# ---------------------------
# Example: count values in a column
if "Category" in df.columns:
    print("\nCategory Counts:")
    print(df["Category"].value_counts())

# ---------------------------
# 4. Visualization
# ---------------------------

# Histogram of a numerical column (replace with your column name)
if "Age" in df.columns:
    plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

# Bar chart of categories
if "Category" in df.columns:
    df["Category"].value_counts().plot(kind="bar", color="lightgreen")
    plt.title("Category Counts")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()

# Scatter plot of two columns (replace with numeric columns in your dataset)
if "Age" in df.columns and "Salary" in df.columns:
    plt.scatter(df["Age"], df["Salary"], color="orange")
    plt.title("Age vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.show()

# ---------------------------
# 5. Findings / Observations
# ---------------------------
# Print observations manually or add logic
print("\nObservations:")
print("- The dataset contains", df.shape[0], "rows and", df.shape[1], "columns.")
print("- Numerical features show basic statistical trends using describe().")
print("- Visualizations reveal distributions and relationships between variables.")
