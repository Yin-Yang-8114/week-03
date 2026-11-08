class Book:
    total_books = 0
    def __init__(self, title, author,copies):
        if copies <=0:
            raise ValueError('cant be empty')
        self.title = title
        self.author = author
        self.copies = copies
        self.available = copies
        Book.total_books +=1

    def borrow(self):
        if self.available > 0:
            self.available -= 1
            return True
        else:
            raise ValueError("no copies left")
        
    def return_book(self):
        if self.available == self.copies:
            raise ValueError ("all books are in")
        self.available += 1

    def is_available(self):
        return self.available > 0
    
    def __str__(self):
        return f"{self.title} by {self.author}, Available copies: {self.available} out of {self.copies}"


books = [
    Book("Clean Code", "Martin", 3),
    Book("Python Basics", "Cohen", 1),
]

books[0].borrow()
books[1].borrow()

try:
    books[1].borrow()
except ValueError as error:
    print("Python Basics ->", error)

try:
    Book("Empty", "Nobody", 0)
except ValueError as error:
    print("Empty ->", error)

for book in books:
    print(book, "| available:", book.is_available())

print("Books in the library:", Book.total_books)
