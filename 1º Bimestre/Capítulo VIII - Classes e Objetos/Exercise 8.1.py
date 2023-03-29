class Person():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def dataShow(self):
        print(f'{self.name} have {self.age} years old')

person1 = Person(input('Your name: '), int(input('Your age: ')))
person2 = Person(input('Your name: '), int(input('Your age: ')))

person1.dataShow()
person2.dataShow()