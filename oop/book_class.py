class Book:
  """
  A class representing a book with title, author, and publication year attributes.
  """

  def __init__(self, title: str, author: str, year: int):
    """
    Initializes a Book instance with title, author, and year.

    Args:
      title: The title of the book.
      author: The author of the book.
      year: The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints "Deleting (title of the book)" upon object deletion.
    """
    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a string in the format "(title) by (author), published in (year)".

    Returns:
      A string representation of the book.
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string that would recreate the Book instance:
    f"Book('{self.title}', '{self.author}', {self.year})".

    Returns:
      A string representation of the Book object for recreation.
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
