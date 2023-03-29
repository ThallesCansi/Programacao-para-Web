class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def dataShow(self):
        print(f'{self.name} have {self.age} years old')

class Employee(Person):
    def __init__(self, name: str, age: int, salary: float) -> None:
        super().__init__(name, age)
        self.salary = salary

    def increaseSalary(self, percentage: int):
        self.increase = (percentage / 100) * self.salary
        self.salary += self.increase
    
    def dataShow(self):
        super().dataShow()
        print(f'Old salary: $ {(self.salary - self.increase):.2f}')
        print(f'Increase: $ {self.increase}')
        print(f'New salary: $ {self.salary:.2f}')

employee1 = Employee(input('Your name: '),
                   int(input('Your age: ')), 
                   float(input('Enter your salary: $ ')))

employee1.increaseSalary(int(input('Enter your raise: ')))
employee1.dataShow()