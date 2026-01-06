import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\4th week project\code\Sales_Data.csv")

# Cleaning
df['Date'] = pd.to_datetime(df['Date'])
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)
df['Price'].fillna(df['Price'].mean(), inplace=True)

# Feature engineering
df['Total_Sales'] = df['Quantity'] * df['Price']

# Monthly sales trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure()
plt.plot(monthly_sales.index.astype(str), monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
