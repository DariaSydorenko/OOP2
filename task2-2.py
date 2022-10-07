import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument('-a', type=int)
parser.add_argument('-b', type=int)
args = parser.parse_args()


class Rational:
    def __init__(self, numerator, denominator):
        if numerator is None:
            numerator = 1
        if denominator is None:
            denominator = 1
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError
        if denominator == 0:
            raise ZeroDivisionError
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd

    def set_numerator(self, n):
        self.numerator = n

    def set_denominator(self, d):
        self.denominator = d

    def print_rational(self):
        return str(f"{int(self.numerator)}/{int(self.denominator)}")

    def print_float(self):
        return self.numerator/self.denominator


result = Rational(args.a, args.b)
print(result.print_rational())
print(result.print_float())


