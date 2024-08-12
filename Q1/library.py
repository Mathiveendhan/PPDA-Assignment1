import os
import json
from datetime import datetime

from book import Book
from user import User
from transaction import Transaction

class Library:
    def __init__(self, books_file='books.json', users_file='users.json', transactions_file='transactions.json'):
        self.books_file = books_file
        self.users_file = users_file
        self.transactions_file = transactions_file
        self.books = self.load_books()
        self.users = self.load_users()
        self.transactions = self.load_transactions()

    def load_books(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as file:
                return {book_id: Book.from_dict(book) for book_id, book in json.load(file).items()}
        return {}

    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                return {user_id: User.from_dict(user) for user_id, user in json.load(file).items()}
        return {}

    def load_transactions(self):
        if os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'r') as file:
                return {transaction_id: Transaction.from_dict(transaction) for transaction_id, transaction in json.load(file).items()}
        return {}

    def save_books(self):
        with open(self.books_file, 'w') as file:
            json.dump({book_id: book.to_dict() for book_id, book in self.books.items()}, file)

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump({user_id: user.to_dict() for user_id, user in self.users.items()}, file)

    def save_transactions(self):
        with open(self.transactions_file, 'w') as file:
            json.dump({transaction_id: transaction.to_dict() for transaction_id, transaction in self.transactions.items()}, file)

    def add_book(self, title, author):
        book_id = str(len(self.books) + 1)
        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        self.save_books()
        print(f"Book '{title}' by {author} added successfully with ID {book_id}.")

    def register_user(self, name):
        user_id = str(len(self.users) + 1)
        new_user = User(user_id, name)
        self.users[user_id] = new_user
        self.save_users()
        print(f"User '{name}' registered successfully with ID {user_id}.")

    def borrow_book(self, user_id, book_id):
        if book_id not in self.books or user_id not in self.users:
            print("Invalid book ID or user ID.")
            return
        book = self.books[book_id]
        if not book.available:
            print(f"Book '{book.title}' is currently not available.")
            return
        transaction_id = str(len(self.transactions) + 1)
        new_transaction = Transaction(transaction_id, user_id, book_id, datetime.now().strftime('%Y-%m-%d'))
        self.transactions[transaction_id] = new_transaction
        book.available = False
        self.save_books()
        self.save_transactions()
        print(f"Book '{book.title}' borrowed successfully by user '{self.users[user_id].name}'.")

    def return_book(self, user_id, book_id):
        if book_id not in self.books or user_id not in self.users:
            print("Invalid book ID or user ID.")
            return
        for transaction in self.transactions.values():
            if transaction.user_id == user_id and transaction.book_id == book_id and transaction.date_returned is None:
                transaction.date_returned = datetime.now().strftime('%Y-%m-%d')
                self.books[book_id].available = True
                self.save_books()
                self.save_transactions()
                print(f"Book '{self.books[book_id].title}' returned successfully by user '{self.users[user_id].name}'.")
                return
        print(f"No active transaction found for user ID {user_id} and book ID {book_id}.")
