nationality = input('Are you Brazilian (y/n): ')
age = int(input('Tell me your age: '))

if (nationality == 'y' and age > 18):
    print('You are eligible to vote')
else:
    print("You aren't eligible to vote")