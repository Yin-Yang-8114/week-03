from data import books
from valdiations import validate_input

def serche_book(books,name): # find()
    books_found = []
    for book in books:
        if name.lower() in book["name"].lower():
            books_found.append(book)
    if books_found:
        print("Books found:")
        for book in books_found:
            print(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Year: {book['year']}, Availability: {'Available' if book['available'] else 'Not Available'}")
    else:
        print("No books found with that name.")



def add_book(books,name,author,year):
    new_book = {
        "id": get_next_book_id(books),
        "name": name,
        "author": author,
        "year": year,
        "available": True}
    if any(book["name"].lower() == name.lower() for book in books) and any(book["author"].lower() == author.lower() for book in books):
        print(f"Book '{name}' by '{author}' already exists in the library.")
        return
    books.append(new_book)
    print(f"Book '{name}' added successfully.")


def borrow_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print(f"You have borrowed '{book['name']}'.")
            else:
                print(f"Sorry, '{book['name']}' is currently not available.")
            return
    print("Book not found.")

def return_book(books, book_id):
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print(f"You have returned '{book['name']}'.")
            else:
                print(f"'{book['name']}' was not borrowed.")
            return
    print("Book not found.")


def get_available_books(books):
    available_books = [book for book in books if book["available"]]
    if not available_books:
        print("No available books found.")
        return
    print("Available books:")
    for book in available_books:
        print(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Year: {book['year']}")

def get_books_by_author(books, author):
    books_found = []
    for book in books:
        if author.lower() == book["author"].lower():
            books_found.append(book)
    if books_found:
        print("Books found:")
        for book in books_found:
            print(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Year: {book['year']}, Availability: {'Available' if book['available'] else 'Not Available'}")
    else:
        print("No books found with that author.")

def get_next_book_id(books):
    return len(books) +1