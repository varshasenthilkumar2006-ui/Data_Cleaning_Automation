# ======================================================
# Data Cleaning & Reporting Automation Project
# ======================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("===== Data Cleaning & Reporting Automation Started =====\n")

# -------------------------------
# 1. Create Sample Dirty Data (Real-world example)
# -------------------------------
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 102, 111],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Rahul', 'Anjali', 'Vikram', None, 'Sneha', 'Karan', 'Priya', 'Divya'],
    'Age': [25, 30, np.nan, 28, 25, 35, 40, 22, 28, np.nan, 30, 27],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'male', 'Female', 'Female', 'Male', 'Female', 'Female'],
    'City': ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'chennai', 'Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Pune', 'Mumbai', 'Hyderabad'],
    'Purchase_Amount': [1500, 2300, 1800, 1200, 1500, 3000, 2500, 900, 1200, 2000, 2300, 1700],
    'Join_Date': ['2023-01-15', '2023-02-20', '2023-01-10', '2023-03-05', '2023-01-15', '2023-04-12', '2023-02-28', '2023-05-01', '2023-03-05', '2023-06-18', '2023-02-20', '2023-07-22']
}

df = pd.DataFrame(data)

print("===== Original Dirty Data =====")
print(df)
print("\nShape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# -------------------------------
# 2. Data Cleaning Steps
# -------------------------------

# 2.1 Remove Duplicates
df_clean = df.drop_duplicates()
print("\nAfter removing duplicates:", df_clean.shape)

# 2.2 Handle Missing Values
df_clean['Name'] = df_clean['Name'].fillna('Unknown')
df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())

# 2.3 Fix Inconsistent Data (Gender & City)
df_clean['Gender'] = df_clean['Gender'].str.capitalize()
df_clean['City'] = df_clean['City'].str.title()

# 2.4 Convert Date column
df_clean['Join_Date'] = pd.to_datetime(df_clean['Join_Date'])

print("\n===== Cleaned Data =====")
print(df_clean)
print("\nMissing Values after cleaning:\n", df_clean.isnull().sum())

# -------------------------------
# 3. Automated Summary Report
# -------------------------------
print("\n" + "="*50)
print("           AUTOMATED SUMMARY REPORT")
print("="*50)

print(f"\nTotal Customers        : {df_clean.shape[0]}")
print(f"Average Age            : {df_clean['Age'].mean():.1f} years")
print(f"Total Purchase Amount  : ₹{df_clean['Purchase_Amount'].sum():,}")
print(f"Average Purchase       : ₹{df_clean['Purchase_Amount'].mean():.0f}")
print(f"Male Customers         : {(df_clean['Gender']=='Male').sum()}")
print(f"Female Customers       : {(df_clean['Gender']=='Female').sum()}")

print("\nTop Cities by Customers:")
print(df_clean['City'].value_counts().head(5))

# -------------------------------
# 4. Visual Summary (Automated Charts)
# -------------------------------

# Chart 1: Gender Distribution
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.countplot(x='Gender', data=df_clean, palette='Set2')
plt.title('Gender Distribution')

# Chart 2: Purchase by City
plt.subplot(1, 2, 2)
sns.barplot(x='City', y='Purchase_Amount', data=df_clean, estimator=sum, palette='viridis', ci=None)
plt.title('Total Purchase by City')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Chart 3: Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df_clean['Age'], kde=True, color='skyblue')
plt.title('Age Distribution of Customers')
plt.show()

# -------------------------------
# 5. Save Cleaned Data
# -------------------------------
df_clean.to_csv("Cleaned_Customer_Data.csv", index=False)
print("\nCleaned data saved as 'Cleaned_Customer_Data.csv'")

print("\n===== Data Cleaning & Reporting Automation Completed Successfully! =====")