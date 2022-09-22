import argparse
parser = argparse.ArgumentParser(description='expression')
parser.add_argument('x1', type=float, help='the first value')
parser.add_argument('operation', type=str, help='operation for x1, x2')
parser.add_argument('x2', type=float, help='the second value')
args = parser.parse_args()


def addition(x1, x2):
    return x1 + x2


def subtraction(x1, x2):
    return x1 - x2


def multiplication(x1, x2):
    return x1 * x2


def division(x1, x2):
    return x1 / x2


calculator = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}

result = calculator.get(args.operation)
if result:
    print(result(args.x1, args.x2))
else:
    print('Error')
