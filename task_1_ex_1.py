"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", help="Number1 to calculate", type=float)
parser.add_argument("command", help="operation name")
parser.add_argument("num2", help="Number2 to calculate", type=float)


def calculate(args):
    args = parser.parse_args()
    if args.command == '+':
        return (args.num1 + args.num2)
    elif args.command == "-":
        return (args.num1 - args.num2)
    elif args.command == "/":
        if args.num1 == 0 or args.num2 == 0:
            raise ZeroDivisionError()
        else:
            return (args.num1 / args.num2)
    elif args.command == "*":
        return (args.num1 * args.num2)
    else:
        raise NotImplementedError()
    pass


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
