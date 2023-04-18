class Car:
    def __init__(self, speed: float) -> None:
        self.speed = speed
    
    def accelerate(self, seconds: int):
        print(f'Current speed: {self.speed} m/s')
        self.speed += 10 * seconds
        print(f'Accelerated for {seconds} seconds and reached {self.speed:.2f} m/s')

    def brake(self, seconds: int):
        print(f'Current speed: {self.speed} m/s')
        slowdown = 5 * seconds
        if self.speed > slowdown:
            self.speed -= slowdown
            print(f'Braked for {seconds} seconds and reched {self.speed:.2f} m/s')
        else:
            self.speed = 0
            print('You stopped the car completely')

car1 = Car(float(input('Enter car speed (m/s): ')))
car1.accelerate(int(input('Enter the time in seconds that the car accelerated: ')))
car1.brake(int(input('Enter the time in seconds that the car braked: ')))