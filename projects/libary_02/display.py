def display_menu():
        print("===============================")
        print("       LIBRARY MANAGEMENT")
        print("================================")
        print("\n1. Display all books")
        print("2. Search book by name")
        print("3. Add new book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Display available books")
        print("7. Display books by author")
        print("8. Exit")

def display_books(books):
    if not books:
        print("No books found.")
        return
    for book in books:
        availability = "Available" if book["available"] else "Not Available"
        print(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Year: {book['year']}, Availability: {availability}")