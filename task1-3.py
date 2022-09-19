import argparse
import sys
parser = argparse.ArgumentParser(description='math example')
parser.add_argument('-y', type=str, help='example')
args = parser.parse_args()
if args.y == None:
    print('{}, {}'.format('False', 'None'))
    sys.exit()
x = list(args.y)
i = 0
fl = 1
while i < len(x):
    if i == 0 and not x[0].isnumeric():
        fl = 0
        break
    elif i > 0 and x[i] != '+' and x[i] != '-' and not x[0].isnumeric():
        fl = 0
        break
    elif i > 0 and (x[i] == '+' or x[i] == '-') and (x[i-1] == '+' or x[i-1] == '-'):
        fl = 0
        break
    else:
        i = i + 1
        continue
if fl:
    print('{}, {}'.format('True', eval(args.y)))
else:
    print('{}, {}'.format('False', 'None'))
