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

    def borrow_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False
