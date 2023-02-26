from os import system
system('clear')

vowels = ['a', 'e', 'i', 'o', 'u']

letter = input('Type a letter: ')

if (letter in vowels):
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')