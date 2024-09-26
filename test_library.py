# test_library.py
import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.assertTrue(self.library.add_book(book))
        self.assertIn(book, self.library.books)

    def test_add_duplicate_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.library.add_book(book)
        self.assertFalse(self.library.add_book(book))

    def test_borrow_available_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.library.add_book(book)
        self.assertTrue(self.library.borrow_book("123456789"))

    def test_borrow_unavailable_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.library.add_book(book)
        self.library.borrow_book("123456789")
        self.assertFalse(self.library.borrow_book("123456789"))

    def test_return_borrowed_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.library.add_book(book)
        self.library.borrow_book("123456789")
        self.assertTrue(self.library.return_book("123456789"))
        self.assertFalse(book.is_borrowed)

    def test_return_unborrowed_book(self):
        book = Book("123456789", "Test Book", "Test Author", 2023)
        self.library.add_book(book)
        self.assertFalse(self.library.return_book("123456789"))


if __name__ == '__main__':
    unittest.main()
