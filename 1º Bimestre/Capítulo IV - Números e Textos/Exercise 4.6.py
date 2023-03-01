import math

a1 = int(input('Type 1st expression complex number (real): '))
a2 = int(input('Type 1st expression complex number (imaginary): '))
b1 = int(input('Type 2st expression complex number (real): '))
b2 = int(input('Type 2st expression complex number (imaginary): '))

complexSum = complex(a1, a2) + complex(b1, b2)
complexMult = complex(a1, a2) * complex(b1, b2)

print(f'The sum of the {complex(a1, a2)} with {complex(b1, b2)} is equal to: {complexSum}')
print(f'The multiplication of the {complex(a1, a2)} with {complex(b1, b2)} is equal to: {complexMult}')