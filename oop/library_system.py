class Book:
  """
  A base class representing a book with title and author attributes.
  """

  def __init__(self, title: str, author: str):
    """
    Initializes a Book instance with title and author.

    Args:
      title: The title of the book.
      author: The author of the book.
    """
    self.title = title
    self.author = author


class EBook(Book):
  """
  A derived class representing an Ebook with additional file size attribute.
  """

  def __init__(self, title: str, author: str, file_size: int):
    """
    Initializes an EBook instance with title, author, and file size.

    Args:
      title: The title of the Ebook.
      author: The author of the Ebook.
      file_size: The file size of the Ebook in MB.
    """
    super().__init__(title, author)
    self.file_size = file_size


class PrintBook(Book):
  """
  A derived class representing a PrintBook with additional page count attribute.
  """

  def __init__(self, title: str, author: str, page_count: int):
    """
    Initializes a PrintBook instance with title, author, and page count.

    Args:
      title: The title of the PrintBook.
      author: The author of the PrintBook.
      page_count: The number of pages in the PrintBook.
    """
    super().__init__(title, author)
    self.page_count = page_count


class Library:
  """
  A class representing a library that manages a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library instance with an empty list to store books.
    """
    self.books = []

  def add_book(self, book: Book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.

    Args:
      book: A Book, EBook, or PrintBook instance.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library collection.
    """
    for book in self.books:
      if isinstance(book, EBook):
        print(f"E-Book - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}MB")
      elif isinstance(book, PrintBook):
        print(f"Print Book - Title: {book.title}, Author: {book.author}, Page Count: {book.page_count} pages")
      else:
        print(f"Book - Title: {book.title}, Author: {book.author}")

        class Book:
  """
  A base class representing a book with title and author attributes.
  """

  def __init__(self, title: str, author: str):
    """
    Initializes a Book instance with title and author.

    Args:
      title: The title of the book.
      author: The author of the book.
    """
    self.title = title
    self.author = author


class EBook(Book):
  """
  A derived class representing an Ebook with additional file size attribute.
  """

  def __init__(self, title: str, author: str, file_size: int):
    """
    Initializes an EBook instance with title, author, and file size.

    Args:
      title: The title of the Ebook.
      author: The author of the Ebook.
      file_size: The file size of the Ebook in MB.
    """
    super().__init__(title, author)
    self.file_size = file_size


class PrintBook(Book):
  """
  A derived class representing a PrintBook with additional page count attribute.
  """

  def __init__(self, title: str, author: str, page_count: int):
    """
    Initializes a PrintBook instance with title, author, and page count.

    Args:
      title: The title of the PrintBook.
      author: The author of the PrintBook.
      page_count: The number of pages in the PrintBook.
    """
    super().__init__(title, author)
    self.page_count = page_count


class Library:
  """
  A class representing a library that manages a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library instance with an empty list to store books.
    """
    self.books = []

  def add_book(self, book: Book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.

    Args:
      book: A Book, EBook, or PrintBook instance.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library collection.
    """
    for book in self.books:
      if isinstance(book, EBook):
        print(f"E-Book - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}MB")
      elif isinstance(book, PrintBook):
        print(f"Print Book - Title: {book.title}, Author: {book.author}, Page Count: {book.page_count} pages")
      else:
        print(f"Book - Title: {book.title}, Author: {book.author}")
