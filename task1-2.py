import argparse
parser = argparse.ArgumentParser(description='expression')
parser.add_argument('operation', type=str, help='operation for x1, x2')
parser.add_argument('x1', type=float, help='the first value')
parser.add_argument('x2', type=float, help='the second value')
args = parser.parse_args()
if args.operation == 'add':
    print(args.x1+args.x2)
elif args.operation == 'subtract':
    print(args.x1-args.x2)
elif args.operation == 'multiply':
    print(args.x1*args.x2)
elif args.operation == 'divide':
    print(args.x1/args.x2)
else:
    print('Error')
