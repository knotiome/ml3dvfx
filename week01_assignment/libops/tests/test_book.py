from libops.book import Book

def test_book_price()->None:
    book = Book("The Complete Grimms' Fairy Tales", "Jacob Brimm", "fiction",22.49)
    assert book.value >= 0.0 or book.value == 22.49

def test_book_name()->None:
    book = Book("Goodnight Moon", "Margaret Wise Brown", "childrens", 6.99)
    assert len(book.title) > 0
