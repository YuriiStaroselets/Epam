import argparse

parser = argparse.ArgumentParser()
parser.add_argument("revs", help="given integer n calculate", type=float)


def calculate(args):

    n = args.revs

    if args.revs > 0:
        result = n * n
        return result
    elif args.revs < 0:
        result = n * (-1)
        return result
    elif args.revs == 0:
        return 0


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()