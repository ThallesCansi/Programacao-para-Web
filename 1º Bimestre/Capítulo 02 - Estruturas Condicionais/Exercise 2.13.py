age = int(input('Tell me your age: '))
gender = input('Say your sex (m/f): ').lower()

if (gender == 'm' and age >= 65):
    print('You are eligible for retirement')
elif (gender == 'f' and age >= 60):
    print('You are eligible for retirement')
else:
    print("You aren't eligible for retirement")