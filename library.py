# library.py
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not self.find_book_by_isbn(book.get_isbn()):
            self.books.append(book)
            return True
        return False

    def find_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.get_isbn() == isbn), None)
