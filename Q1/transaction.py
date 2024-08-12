from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, user_id, book_id, date_borrowed, date_returned=None):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
        self.date_borrowed = date_borrowed
        self.date_returned = date_returned

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'date_borrowed': self.date_borrowed,
            'date_returned': self.date_returned
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data['transaction_id'], data['user_id'], data['book_id'], data['date_borrowed'], data['date_returned'])
