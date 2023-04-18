from playsound import playsound

class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def makeSound(self):
        print(f'{self.name.capitalize()} sound')
        playsound(f'sounds/{self.name}.mp3')

animal1 = Animal(input('Enter the name of the animal: '), int(input('Enter the age of the animal: ')))
animal1.makeSound()