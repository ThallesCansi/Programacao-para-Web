height = float(input('Tell me your height (cm): '))
weight = float(input('Tell me your weight now (kg): '))

bmi = weight / (height ** 2)

if (bmi < 18.5):
    print('You are underweight')
elif (bmi < 24.9):
    print('You are at normal weight')
else:
    print('You are obese')