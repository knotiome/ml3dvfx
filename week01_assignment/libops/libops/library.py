import json
from dataclasses import dataclass, field
from libops.book import Book
from libops.random_utilities import RandomUtilities

@dataclass
class Library:
    isEmpty: bool = True
    isActive: bool = False
    id: str = field(init=False, default_factory=RandomUtilities.generate_ISBN)

    @staticmethod
    def load_json_files(path) -> dict:
        """
        Read json files from a directory.

        Args:
            path: the path for the json file ro read.
        Returns:
            dict: A hash map with the json structure.
        """
        with open(path, "rb") as data_file:
            data_file = json.load(data_file)

        return data_file
    
    @staticmethod
    def print_json_structure(data_file):
        for id, item in data_file["Books"].items():
            print(id, item)

    def get_all_books(self, verbose=0)->dict:
        """
        Reads and returns a hash map with all the available books

        Args:
            if verbose is set to 1, it will print all the books.

        Returns:
            dict: a hash map with all the books in the database.
        """
        data_file = self.load_json_files("./datapile.json")

        if len(data_file.items()) > 0:
            self.isEmpty = False
            self.isActive = True

        try:
            if verbose == 1:
                self.print_json_structure(data_file)
                return data_file
            else:
                return data_file

        except:
            raise ValueError("The value for the verbose as to be 0 or 1")

    def search_books(self, query: str)->list[Book]:
        """
        """
        data = self.load_json_files("./datapile.json")
        matching_books = []
        for book_id, book_data in data["Books"].items():
            book = Book(title=book_data["title"], author=book_data["author"], genre=book_data["genre"], _value=book_data["value"], isbn=book_id)
            if query.lower() in book.search_string.lower():
                matching_books.append(book)

        if len(matching_books) == 0:
            print("No books found")

        else:
            for book in matching_books:
                print(f"Found: {book.title} {book.author} {book.genre} ${book.value}")

        return matching_books

    def get_total_book_count(self)->int:
        """
        Returns the total number of books in the stack.

        Returns:
            int: The total number of books in the stack.
        """
        data = self.get_all_books()
        return len(data["Books"].items())

    def add_book_to_stack(self, book: Book):
        """
        Adds a book to the stack and updates the database.json file.

        Args:
            book (Book): The item to add to the cart.
        """
        data = self.get_all_books()

        new_book = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "value": book.value
        }

        data["Books"][book.isbn] = new_book

        with open("./datapile.json", 'w') as file:
            json.dump(data, file, indent=4)

        self.isEmpty = False
        self.isActive = True

        print(f"Added {book.title} to the stack.")

    def remove_books_from_stack_by_query(self, query: str):
        """
        Removes all the instances of a book from the stack based on a query.

        Args:
            query (str): The search query to find the book to remove.
        """
        data = self.get_all_books()
        books_to_remove = []

        for book_id, book_data in data["Books"].items():
            if query.lower() in book_data["title"].lower() or query.lower() in book_data["genre"].lower():
                books_to_remove.append(book_id)

        if not books_to_remove:
            print(f"No books found matching '{query}'")
            return

        for book_id in books_to_remove:
            book_title = data["Books"][book_id]["title"]
            del data["Books"][book_id]
            print(f"Removed {book_title} from the cart.")

        with open("./datapile.json", 'w') as file:
            json.dump(data, file, indent=4)

        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

    def remove_books_from_stack_by_selection(self):
        """
        Removes the selected book by index.
        """

        data = self.get_all_books()
        books = []
        i = 1
        for book_id, book_data in data["Books"].items():
            books.append(book_id)
            print(f"{i}: {book_data}")
            i += 1
        try:
            usr_choice = int(input("Select the book to delete by number, example: 1: ")) - 1
        except:
            raise ValueError("You must select a valid number!")

        if usr_choice > len(books):
            print("Book not found!")
            return

        book_to_delete = books[usr_choice]
        book_title = data["Books"][book_to_delete]["title"]
        del data["Books"][book_to_delete]
        print(f"Removed {book_title} from the stack.")

        with open("./datapile.json", 'w') as file:
            json.dump(data, file, indent=4)

        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

    def get_total_value_of_books(self)->float:
        """"
        Returns:
            float: the total price for all the books in the stack.
        """
        data = self.get_all_books()
        total_value = 0

        for book_id, book_data in data["Books"].items():
            total_value += data["Books"][book_id]["value"]

        return total_value

    def empty_stack(self):
        """
        Clear all the books in the stack.
        """
        data = self.get_all_books()
        if len(data["Books"].items()) > 0:
            data = {"Books":{}}

            with open("./datapile.json", 'w') as file:
                json.dump(data, file, indent=4)

            if not data["Books"]:
                self.isEmpty = True
                self.isActive = False
            print("The stack is empty")
        else:
            print("The stack is already empty")

