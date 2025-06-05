from libops.book import Book
from libops.library import Library

if __name__ == "__main__":

    #the main database for the cart to pass to the class
    database = "./datapile.json"
    my_stack = Library()

    #search for an item
    print("Searching item...")
    results = my_stack.search_books("Membrane Structures")
    print("------------------------")

    #get the total amount of items in the cart
    print("Total items in the current cart:")
    total_item_count = my_stack.get_total_book_count()
    print(f"Total items count: {total_item_count}")

    print("------------------------")

    #Create a Book object so it can be added to the stack
    print("Adding items to the cart:...")
    print("------------------------")
    atlas = Book("World Atlas", "National Geographic Society", "reference", 21.50)
    my_stack.add_book_to_stack(atlas)
    dictionary = Book("The Merriam-Webster Dictionary", "Merriam-Webster", "reference", 24.99)
    my_stack.add_book_to_stack(dictionary)

    #get all the books in the stack
    print("------------------------")
    print("Getting all the books in the stack:")
    print("------------------------")
    my_stack.get_all_books(verbose=1)

    print("------------------------")

    #remove all books by title or genre
    print("Removing all instances of a book:")
    print("------------------------")
    my_stack.remove_books_from_stack_by_query("World Atlas")
    print("------------------------")
    print("\n")
    
    #removes a selected book
    print("Removing a specific book by selection:")
    print("------------------------")
    my_stack.remove_books_from_stack_by_selection()
    print("------------------------")

    print("All the current books in the stack:")
    my_stack.get_all_books(verbose=1)
    print("------------------------")

    print("Total value for all the items in the stack:")
    total_value = my_stack.get_total_value_of_books()
    print(f"${total_value}")
