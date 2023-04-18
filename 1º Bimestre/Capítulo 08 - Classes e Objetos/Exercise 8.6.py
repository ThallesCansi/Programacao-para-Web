import math

class Circle():
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self):
        pi = math.pi
        area = pi * math.pow(self.radius, 2)
        print(f'Circle area: {area:.2f}')

circle1 = Circle(float(input('Enter the radius of the circle: ')))
circle1.area()