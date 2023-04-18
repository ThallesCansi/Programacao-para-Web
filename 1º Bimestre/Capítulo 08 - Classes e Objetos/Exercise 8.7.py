personList = list()

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

    def dataShow(self):
        super().dataShow()
        print(f'Salary: $ {self.salary:.2f}')

personList.append(Person(input('Your name: '), int(input('Your age: '))))
personList.append(Employee(input('Your name: '),
                           int(input('Your age: ')), 
                           float(input('Enter your salary: $ '))))

for i in personList:
    i.dataShow()
