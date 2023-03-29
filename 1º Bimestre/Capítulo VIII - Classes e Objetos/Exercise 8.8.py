class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def dataShow(self):
        print(f'{self.name} have {self.age} years old')

class Student(Person):
    def __init__(self, name: str, age: int, id: int) -> None:
        super().__init__(name, age)
        self.id = id

    def dataShow(self):
        super().dataShow()
        print(f'ID: $ {self.id}')

student1 = Student(input('Your name: '),
                   int(input('Your age: ')), 
                   int(input('Enter your ID: ')))

student1.dataShow()