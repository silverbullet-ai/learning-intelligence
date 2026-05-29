class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author

    def display_book(self):

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


book = Book("Python Basics", "Aahish")

book.display_book()