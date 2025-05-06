### Class methods ###
###Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books=0
    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.increment_book_count()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "Geotge Orwell")
print(f"Total books: {Book.total_books}") 