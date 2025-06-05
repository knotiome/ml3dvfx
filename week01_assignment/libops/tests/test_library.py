import pytest
from libops.library import Library
from libops.book import Book

@pytest.fixture
def stack():
    datapile = "./tests/test_datapile.json"
    lib = Library()
    lib.empty_stack()
    return lib

def test_total_value_of_stack(stack):
    book1 = Book("Calculus", "Thomas Finney", "mathematics", 99.99)
    book2 = Book("Figure Drawing: The Structure, Anatomy, and Expressive Design of Human Form", "Nathan Goldstein", "art", 69.99)
    stack.add_book_to_stack(book1)
    stack.add_book_to_stack(book2)
    assert stack.get_total_value_of_books() == 169.98

def test_empty_stack(stack):
    book = Book("James and the Giant Peach", "Roald Dahl", "fiction", 17.99)
    stack.add_book_to_stack(book)
    stack.empty_stack()
    assert len(stack.get_all_books()["Books"].items()) == 0

def test_search_book(stack):
    book = Book("Digital Painting Techniques: Practical Techniques of Digital Art Masters", "3dtotal.com", "computer graphics", 33.99)
    stack.add_book_to_stack(book)
    books_list = stack.search_books("Digital Painting Techniques: Practical Techniques of Digital Art Masters")
    assert books_list[0].title == "Digital Painting Techniques: Practical Techniques of Digital Art Masters"

def test_get_all_books(stack):
    book1 = Book("ZBrush Character Creation: Advanced Digital Sculpting", "Scott Spencer", "computer graphics", 43.99)
    book2 = Book("The Art of Stop-Motion Animation", "Ken A. Priebe", "computer graphics", 55.00)
    stack.add_book_to_stack(book1)
    stack.add_book_to_stack(book2)
    retrieved_books = stack.get_all_books()
    names_to_compare = [book1.title, book2.title]
    results = [book_data["title"] for book_id, book_data in retrieved_books["Books"].items()]
    assert names_to_compare == results

def test_get_total_book_count(stack):
    book1 = Book("The Art and Science of Digital Compositing", "Ron Brinkmann", "computer graphics", 89.99)
    book2 = Book("Of Mice and Magic: A History of American Animated Cartoons", "Leonard Maltin", "nonfiction", 39.99)
    stack.add_book_to_stack(book1)
    stack.add_book_to_stack(book2)
    assert stack.get_total_book_count() == 2
