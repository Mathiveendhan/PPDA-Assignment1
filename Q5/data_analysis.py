import pandas as pd
import matplotlib.pyplot as plt

def analyze_customer_behavior(customers, orders, reviews):
    # Example: Analyze repeat customers
    repeat_customers = orders['customer_id'].value_counts()
    print(f"Number of repeat customers: {len(repeat_customers[repeat_customers > 1])}")

def analyze_product_performance(products, orders, reviews):
    # Example: Analyze top-selling products
    top_selling_products = orders.groupby('product_id')['quantity'].sum().sort_values(ascending=False)
    print(f"Top-selling products:\n{top_selling_products.head()}")

def analyze_sales_trends(orders):
    # Updated to use 'ME' for month-end resampling
    monthly_sales = orders.resample('ME', on='order_date')['price'].sum()
    print(f"Monthly sales trends:\n{monthly_sales}")

def visualize_data(customers, orders, products, reviews):
    # Updated to use 'ME' for month-end resampling
    monthly_sales = orders.resample('ME', on='order_date')['price'].sum()
    plt.plot(monthly_sales.index, monthly_sales.values)
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.show()
