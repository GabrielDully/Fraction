class Fraction(object):
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        
        return f'{self.numerator}/{self.denominator}'
    
    def float_representation(self):
        
        return self.numerator/self.denominator

    def __add__(self, other_fraction):

        if(self.denominator == other_fraction.denominator):
            numerator = self.numerator + other_fraction.numerator
            denominator = self.denominator
        else:
            numerator = self.numerator*other_fraction.denominator + other_fraction.denominator*self.denominator
            denominator = self.denominator*other_fraction.denominator
        
        return Fraction(numerator, denominator)

    def __sub__(self, other_fraction):

        if(self.denominator == other_fraction.denominator):
            numerator = self.numerator - other_fraction.numerator
            denominator = self.denominator
        else:
            numerator = self.numerator*other_fraction.denominator - other_fraction.denominator*self.denominator
            denominator = self.denominator*other_fraction.denominator
        
        return Fraction(numerator, denominator)
    
    def __mul__(self, other_fraction):
        
        numerator = self.numerator*other_fraction.numerator
        denominator = self.denominator*other_fraction.denominator

        return Fraction(numerator, denominator)
    
    def __truediv__(self, other_fraction):
        
        numerator = self.numerator*other_fraction.denominator
        denominator = self.denominator*other_fraction.numerator

        return Fraction(numerator, denominator) 