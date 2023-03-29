class Rectangle:
    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        print(f'Area: {area:.2f}')

class Square(Rectangle):
    def __init__(self, height: float) -> None:
        super().__init__(height, width = height)

square1 = Square(float(input('Enter the side of the square: ')))
square1.area()