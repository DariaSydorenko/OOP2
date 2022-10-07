import argparse
import math
import operator
parser = argparse.ArgumentParser(description='expression')
parser.add_argument('operation', type=str, help='operation for x1, x2')
parser.add_argument('x1', type=float, help='the first value')
parser.add_argument('x2', type=float, help='the second value')
args = parser.parse_args()


def func():
    return getattr(operator, args.operation, False) or getattr(math, args.operation, False)


if func():
    if args.x2 == 0 and args.operation == 'truediv':
        raise ZeroDivisionError
    else:
        result = getattr(operator, args.operation)
        print(result(args.x1, args.x2))
else:
    print('There is no such function')
