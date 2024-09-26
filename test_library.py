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

if __name__ == '__main__':
    unittest.main()
