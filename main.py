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
            sum_numerator = self.numerator + other_fraction.numerator
            sum_denominator = self.denominator
        else:
            sum_numerator = self.numerator*other_fraction.denominator + other_fraction.denominator*self.denominator
            sum_denominator = self.denominator*other_fraction.denominator
        
        return Fraction(sum_numerator, sum_denominator)

    def __sub__(self, other_fraction):

        if(self.denominator == other_fraction.denominator):
            difference_numerator = self.numerator - other_fraction.numerator
            difference_denominator = self.denominator
        else:
            difference_numerator = self.numerator*other_fraction.denominator - other_fraction.denominator*self.denominator
            difference_denominator = self.denominator*other_fraction.denominator
        
        return Fraction(difference_numerator, difference_denominator)
    
    def __mul__(self, other_fraction):
        
        product_numerator = self.numerator*other_fraction.numerator
        product_denominator = self.denominator*other_fraction.denominator

        return Fraction(product_numerator, product_denominator)
    
    def __truediv__(self, other_fraction):
        
        quotient_numerator = self.numerator*other_fraction.denominator
        quotient_denominator = self.denominator*other_fraction.numerator

        return Fraction(quotient_numerator, quotient_denominator) 