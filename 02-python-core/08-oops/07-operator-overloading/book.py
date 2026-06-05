class Book:

    def __init__(
        self,
        title,
        author
    ):

        self.title = title
        self.author = author

    def __eq__(self, other):

        return (
            self.title == other.title
            and
            self.author == other.author
        )

    def __repr__(self):

        return (
            f"Book("
            f"title='{self.title}', "
            f"author='{self.author}')"
        )


book1 = Book(
    "Atomic Habits",
    "James Clear"
)

book2 = Book(
    "Atomic Habits",
    "James Clear"
)

print(book1 == book2)