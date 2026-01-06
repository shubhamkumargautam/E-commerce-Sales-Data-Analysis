import pandas as pd
import matplotlib.pyplot as plt

# 1.Load data
df = pd.read_csv(r"C:\Users\shubh\Desktop\Arena projects file document\4th week project\code\Sales_Data.csv")


# 2. Data Cleaning
df.drop_duplicates(inplace=True)
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)
df['Price'].fillna(df['Price'].mean(), inplace=True)

# 3. Feature Engineering
df['Total_Sales'] = df['Quantity'] * df['Price']

# 4. Bar Chart: Total Sales by Product Category
category_sales = df.groupby('Product')['Total_Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
