class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print(f'The perimeter equals {perimeter}')

class RightTriangle(Triangle):
    def __init__(self, side1: float, side2: float, side3: float, height: float):
        super().__init__(side1, side2, side3)
        self.height = height

    def area(self):
        area = (self.side1 * self.height) / 2
        print(f'The area of the right triangle is equal to the {area}')

triangle1 = RightTriangle(float(input('Enter the first side of the triangle: ')), 
                          float(input('Enter the second side of the triangle: ')), 
                          float(input('Enter the third side of the triangle: ')), 
                          float(input('Enter the height of the triangle: ')))

triangle1.perimeter()
triangle1.area()