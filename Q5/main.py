import pandas as pd
from data_cleaning import clean_customers, clean_orders, clean_products, clean_reviews
from data_analysis import analyze_customer_behavior, analyze_product_performance, analyze_sales_trends, visualize_data

# Load datasets
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
reviews = pd.read_csv('reviews.csv')

# Clean datasets
customers = clean_customers(customers)
orders = clean_orders(orders)
products = clean_products(products)
reviews = clean_reviews(reviews)

# Perform analysis
analyze_customer_behavior(customers, orders, reviews)
analyze_product_performance(products, orders, reviews)
analyze_sales_trends(orders)

# Visualize data
visualize_data(customers, orders, products, reviews)
    