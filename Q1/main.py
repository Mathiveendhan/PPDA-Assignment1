from library import Library

if __name__ == "__main__":
    library = Library()

    # Adding Books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("Pride and Prejudice", "Jane Austen")
    library.add_book("Moby-Dick", "Herman Melville")
    library.add_book("War and Peace", "Leo Tolstoy")

    # Registering Users
    library.register_user("Mathiveendhan")
    library.register_user("Mathinesan")
    library.register_user("bharaniraja")

    # Borrowing Books
    library.borrow_book("1", "1") 
    library.borrow_book("2", "2")  

    # Returning Books
    library.return_book("1", "1") 
