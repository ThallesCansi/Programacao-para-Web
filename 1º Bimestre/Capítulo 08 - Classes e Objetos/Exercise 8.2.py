class Rectangle:
    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        print(f'Rectangle area: {area:.2f}')

rectagle1 = Rectangle(float(input('Enter the height of the rectangle: ')), 
                      float(input('Enter the width of the rectangle: ')))

rectagle1.area()