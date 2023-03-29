from playsound import playsound

class Animal:
    def __init__(self,  name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        print(f'{self.name.capitalize()} sound')
        playsound(f'sounds/{self.name}.mp3')

animal1 = Dog(input('Enter the name of the animal: '))
animal1.makeSound()