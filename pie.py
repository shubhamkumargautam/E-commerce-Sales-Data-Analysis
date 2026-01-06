import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\4th week project\code\Sales_Data.csv")

# Data cleaning
df.drop_duplicates(inplace=True)
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)
df['Price'].fillna(df['Price'].mean(), inplace=True)

# Feature engineering
df['Total_Sales'] = df['Quantity'] * df['Price']

# Pie chart: Sales distribution by category
category_sales = df.groupby('Product')['Total_Sales'].sum()

plt.figure()
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%'
)
plt.title("Sales Distribution by Product Category")
plt.tight_layout()
plt.show()
