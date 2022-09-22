import argparse
parser = argparse.ArgumentParser(description='bars in the bag')
parser.add_argument('-W', type=int, help='weight of the bag')
parser.add_argument('-w', nargs='+', type=int, help='weight of bars')
parser.add_argument('-n', type=int, help='number of bars')
args = parser.parse_args()


def optimal_weight(capacity, weights, bars_number):
    arr = [[0] * (capacity+1) for i in range(bars_number)]
    for i in range(capacity+1):
        if weights[0] < i or weights[0] == i:
            arr[0][i] = weights[0]

    for i in range(bars_number):
        for j in range(capacity+1):
            arr[i][j] = arr[i-1][j]
            if weights[0] < j or weights[0] == j:
                temp = arr[i-1][j-weights[i]] + weights[i]
                if arr[i][j] < temp:
                    arr[i][j] = temp
    return arr[bars_number-1][capacity]


print(optimal_weight(args.W, list(args.w), args.n))
