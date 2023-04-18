import math

class Circle:
    def __init__(self, radius: float):
        self.radius = float(radius)
    
    def areas(self):
        pi = math.pi
        self.area = pi * (math.pow(self.radius, 2))   
        print(f'The area of the circle is equal to: {self.area:.2f}')
    

class Cylinder(Circle):
    def __init__(self, radius: float, height: float):
        super().__init__(radius)
        self.height = height
        
    def volume(self):
        super().areas()
        volume = self.area * self.height
        print(f'The volume of the cylinder is {volume:.2f}')
    
    def areas(self):
        super().areas()
        sideArea = (2 * math.pi * self.radius * self.height)
        areaCylinder = (2 * self.area) + sideArea
        print(f'The area of the cylinder is equal to: {areaCylinder:.2f}')
            
Cylinder1 = Cylinder(float(input('Enter the radius of the cylinder: ')),
                     float(input('Enter the height of the cylinder: ')))
Cylinder1.volume()
Cylinder1.areas()