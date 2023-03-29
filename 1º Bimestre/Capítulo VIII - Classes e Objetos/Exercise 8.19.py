class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def showData(self):
        print(f'The author of book {self.title} is {self.author}')

class LibraryBook(Book):
    def __init__(self, title: str, author: str, id: int) -> None:
        super().__init__(title, author)
        self.id = id

    def showData(self):
        super().showData()
        print(f'The book code {self.title} is {self.id}')

book1 = LibraryBook(input('Enter the title of the book: '), 
                     input('Enter the author of the book: '), 
                     int(input('Enter the book code: ')))

book1.showData()