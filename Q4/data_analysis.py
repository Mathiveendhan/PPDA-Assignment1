import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    customers = pd.read_csv('customers.csv')
    orders = pd.read_csv('orders.csv')
    products = pd.read_csv('products.csv')
    reviews = pd.read_csv('reviews.csv')
    return customers, orders, products, reviews

def clean_data(customers):
    # Handle missing values
    customers['age'] = customers['age'].fillna(customers['age'].median())
    customers['location'] = customers['location'].fillna('Unknown')

    # Convert 'location' to categorical
    customers['location'] = customers['location'].astype('category')

    return customers

def analyze_customer_behavior(orders, customers):
    # Merge orders with customers
    merged = pd.merge(orders, customers, on='customer_id')

    # Calculate total spend per customer
    customer_spend = merged.groupby('customer_id')['price'].sum().sort_values(ascending=False)

    # Display top 10 customers by total spend
    print("Top 10 Customers by Total Spend:")
    print(customer_spend.head(10))

def analyze_product_performance(orders, products):
    # Merge orders with products
    merged = pd.merge(orders, products, on='product_id')

    # Calculate total sales per product using 'price_y' (from products)
    product_sales = merged.groupby('product_id').agg({'price_y': 'sum'})
    product_sales = pd.merge(product_sales, products[['product_id', 'product_name']], on='product_id')

    # Group by product name and sum up sales
    product_sales_summary = product_sales.groupby('product_name')['price_y'].sum().sort_values(ascending=False)

    # Display top 10 products by sales
    print("\nTop 10 Products by Sales:")
    print(product_sales_summary.head(10))

    # Plot product performance
    plt.figure(figsize=(10, 6))
    product_sales_summary.head(10).plot(kind='bar')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Product Name')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()



def analyze_sales_trends(orders):
    # Convert order_date to datetime
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    # Set order_date as index
    orders.set_index('order_date', inplace=True)

    # Resample by month and sum up sales
    monthly_sales = orders.resample('M')['price'].sum()

    # Plot sales trends
    plt.figure(figsize=(12, 6))
    monthly_sales.plot()
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    customers, orders, products, reviews = load_data()
    customers = clean_data(customers)
    analyze_customer_behavior(orders, customers)
    analyze_product_performance(orders, products)
    analyze_sales_trends(orders)

if __name__ == "__main__":
    main()
