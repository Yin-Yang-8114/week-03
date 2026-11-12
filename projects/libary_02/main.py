from valdiations import user_choice,validate_input
from display import display_books
from data import books
from libary_actions import *
def main():
    choice =user_choice()
    while choice != 8:
        if choice == 1:
            display_books(books)
        elif choice == 2:
            name= validate_input("Enter the book name to search: ", "not_empty")
            serche_book(books, name)
        elif choice == 3:
            name = validate_input("Enter the book name: ", "not_empty")
            author = validate_input("Enter the author name: ", "not_empty")
            year = validate_input("Enter the publication year: ", "positive_num")
            add_book(books,name, author, year)
        elif choice == 4:
            book_id = validate_input("Enter the book ID to borrow: ", "positive_num")
            borrow_book(books, book_id)
        elif choice == 5:
            book_id = validate_input("Enter the book ID to return: ", "positive_num")
            return_book(books, book_id)
        elif choice == 6:
            get_available_books(books)
        elif choice == 7:
            author = validate_input("Enter the author name to search: ", "not_empty")
            get_books_by_author(books, author)
        choice = user_choice()
    print("goodbye")


if main() == "__main__":
    main()