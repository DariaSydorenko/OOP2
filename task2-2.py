import math


class Rational:
    def __init__(self, numerator, denominator):
        self.gcd = math.gcd(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, n):
        if not n:
            n = 1
        if not isinstance(n, int):
            raise TypeError
        self.__numerator = n / self.gcd

    @denominator.setter
    def denominator(self, d):
        if d == 0:
            raise ZeroDivisionError
        if not d:
            d = 1
        if not isinstance(d, int):
            raise TypeError
        self.__denominator = d / self.gcd

    def print_rational(self):
        return str(f"{int(self.numerator)}/{int(self.denominator)}")

    def print_float(self):
        return self.numerator/self.denominator


result = Rational(3, 6)
print(result.print_rational())
print(result.print_float())
