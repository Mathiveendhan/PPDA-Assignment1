class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'available': self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data['book_id'], data['title'], data['author'], data['available'])
