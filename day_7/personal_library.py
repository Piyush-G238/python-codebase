class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def __str__(self):
        return f"[title: {self.__title}, author: {self.__author}, year: {self.__year}]"

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

# print(Book("Atomic Habits", "James clear", 2025))
class Library:
    def __init__(self, filename = "library.txt"):
        self.__filename = filename
        self.__books = []
        self.load_books()

    def add_book(self, book):
        self.__books.append(book)
        self.save_books()
        print(f"{book.get_title()} is added to the library!")

    def save_books(self):
        try:
            with open(self.__filename, "w") as f:
                for book in self.__books:
                    f.write(f"{book.get_title()}|{book.get_author()}|{book.get_year()}")
        except Exception as ex:
            print("Error saving books: ", ex)

    def delete_book(self, title):
        for b in self.__books:
            if not b.get_title() == title:
                self.__books.remove(b)
        self.save_books()
        print(f"{title} removed from library!")

    def view_books(self):
        for book in self.__books:
            print(book)

    def search_books(self, title: str):
        for book in self.__books:
            if book.get_title().lower() == title.lower():
                print(book)

    def load_books(self):
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    book_title, author, year = line.strip().split("|")
                    self.__books.append(Book(book_title, author, year))
        except Exception as ex:
            print(f"Error loading books: {ex}")

print("Hi, welcome to my library!")
library = Library()

while True:
    option = 0
    try:
        option = int(input("""
Let me know, how can I help you?
1. Add a book
2. View books
3. Delete a book
4. Search for book
5. Exit
Your option: """))
    except ValueError as e:
        print(f"Unable to parse option, {e}")

    if option == 1:
        input_title = input("Provide title of the book")
        input_author = input("Provide author of the book")
        input_year = input("Provide year of the book")

        library.add_book(Book(input_title, input_author, input_year))

    elif option == 2:
        library.view_books()

    elif option == 3:
        input_title = input("Book to be deleted")
        library.delete_book(input_title)

    elif option == 4:
        input_title = input("Book to be searched")
        library.search_books(input_title)

    elif option == 5:
        print("Thank you for visiting our library!")
        break

    else:
        print("Invalid option. Please try again!")