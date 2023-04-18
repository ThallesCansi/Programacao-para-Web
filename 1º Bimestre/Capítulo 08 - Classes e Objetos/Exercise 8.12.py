class Vehicle:
    def __init__(self, speed: float) -> None:
        self.speed, self.oldSpeed = speed, speed
    
    def accelerate(self, seconds: int):
        self.increase = 10 * seconds
        self.speed += self.increase

    def brake(self, seconds: int):
        self.slowdown = 5 * seconds
        if self.speed > self.slowdown:
            self.speed -= self.slowdown
        else:
            self.speed = 0
    
    def showSpeed(self):
        print(f'Old speed: {self.oldSpeed} m/s')
        print(f'Accelerate: {self.increase} m/s')
        print(f'Brake: {self.slowdown} m/s')
        print(f'New speed: {self.speed} m/s')

class Car(Vehicle):
    def __init__(self, speed: float, brand: str) -> None:
        super().__init__(speed)
        super().accelerate
        super().brake
        self.brand = brand

    def showSpeed(self):
        super().showSpeed()
        print(f'Car brand: {self.brand}')

car1 = Car(float(input('Enter car speed (m/s): ')), input('Enter brand car: '))
car1.accelerate(int(input('Enter the time in seconds that the car accelerated: ')))
car1.brake(int(input('Enter the time in seconds that the car braked: ')))
car1.showSpeed()