class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def dataShow(self):
        print(f'{self.name} have {self.age} years old')

class Client(Person):
    def __init__(self, name: str, age: int, address: str) -> None:
        super().__init__(name, age)
        self.address = address

    def dataShow(self):
        super().dataShow()
        print(f'Address: $ {self.address}')

client1 = Client(input('Your name: '),
                   int(input('Your age: ')), 
                   str(input('Enter your address: ')))

client1.dataShow()