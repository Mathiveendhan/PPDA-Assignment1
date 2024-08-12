import pandas as pd

def clean_customers(customers):
    # Handling missing values in 'age' and 'location' columns
    customers.fillna({'age': customers['age'].median(), 'location': 'Unknown'}, inplace=True)
    # Dropping duplicates
    customers.drop_duplicates(inplace=True)
    return customers

def clean_orders(orders):
    # Convert order dates to datetime
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    # Handling missing values in 'quantity' and 'price'
    orders.fillna({'quantity': 1, 'price': orders['price'].mean()}, inplace=True)
    # Dropping duplicates
    orders.drop_duplicates(inplace=True)
    return orders

def clean_products(products):
    # Handling missing values in 'category' and 'price'
    products.fillna({'category': 'Miscellaneous', 'price': products['price'].mean()}, inplace=True)
    # Dropping duplicates
    products.drop_duplicates(inplace=True)
    return products

def clean_reviews(reviews):
    # Handling missing values in 'rating' and 'review'
    reviews.fillna({'rating': reviews['rating'].median(), 'review': 'No review provided'}, inplace=True)
    # Dropping duplicates
    reviews.drop_duplicates(inplace=True)
    return reviews
