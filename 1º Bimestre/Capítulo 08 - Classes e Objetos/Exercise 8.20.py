class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
    
    def showData(self):
        print(f'{self.numerator} / {self.denominator}')
    
    def multiply(self, anotherFraction):
        newNumerator = self.numerator * anotherFraction.numerator
        newDenominator = self.denominator * anotherFraction.denominator
        return Fraction(newNumerator, newDenominator)
        

fraction1 = Fraction(int(input('Enter the numerator: ')), int(input('enter the denominator: ')))
fraction2 = Fraction(int(input('Enter the numerator: ')), int(input('enter the denominator: ')))

fraction1.showData()  

fraction3 = fraction1.multiply(fraction2)
fraction3.showData()