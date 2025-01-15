# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title  # public attribute
        self.author = author  # public attribute
        self._is_checked_out = False  # private attribute to track if the book is checked out

    # Method to check out the book
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    # Method to return the book
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # Method to check if the book is available
    def is_available(self):
        return not self._is_checked_out

    # String representation of the book for easier printing
    def __str__(self):
        return f"{self.title} by {self.author}"

# Define the Library class
class Library:
    def __init__(self):
        self._books = []  # private list to store books

    # Method to add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Method to check out a book by title
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    # Method to return a book by title
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    # Method to list all available books
    def list_available_books(self):
        available_books = [str(book) for book in self._books if book.is_available()]
        for book in available_books:
            print(book)

# Provided for Testing: main.py

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

