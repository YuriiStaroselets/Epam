"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", "--capacity", help="contains 'capacity' - integer describing the capacity of a knapsack",
                    type=str)
parser.add_argument("-w", "--weights", help=" contains 'weights' - list of weights of each gold bar", nargs='*',
                    type=str)
parser.add_argument("-n", "--bars_number", help="contains 'bars_number' - integer describing the number of gold bars",
                    nargs="?", type=str)


def bounded_knapsack():
    args = parser.parse_args()
    weights = []
    for i in args.weights:
        if i.isdigit():
            weights.append(float(i))
        else:
            raise ValueError
    capacity = []
    for i in args.capacity:
        if i.isdigit():
            capacity.append(float(i))
        else:
            raise ValueError
    if args.bars_number[0].isdigit():
        bars_number = float(args.bars_number)
    else:
        raise ValueError
    if args.capacity[0].isdigit():
        capacity = float(args.capacity)
    else:
        raise ValueError

    capacity1 = capacity

    if len(weights) == bars_number:
        weights.sort(reverse=True)
        count = 0
        for i in weights:
            if capacity > i or capacity==i:
                capacity -= i
                count += 1
        return (capacity1-capacity)
    else:
        raise ValueError


def main():
    print(bounded_knapsack())


if __name__ == '__main__':
    main()