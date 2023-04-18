class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def showData(self):
        print(f'The author of book {self.title} is {self.author}')

class PhysicalBook(Book):
    def __init__(self, title: str, author: str, pages: int) -> None:
        super().__init__(title, author)
        self.pages = pages

    def showData(self):
        super().showData()
        print(f'The number of pages in the book {self.title} is {self.pages}')

book1 = PhysicalBook(input('Enter the title of the book: '), 
                     input('Enter the author of the book: '), 
                     int(input('Enter the number of pages in the book: ')))

book1.showData()