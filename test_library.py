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

    def test_view_available_books(self):
        book1 = Book("123456789", "Test Book", "Test Author", 2023)
        book2 = Book("987654321", "Another Book", "Another Author", 2022)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.borrow_book("123456789")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertIn(book2, available_books)


if __name__ == '__main__':
    unittest.main()
