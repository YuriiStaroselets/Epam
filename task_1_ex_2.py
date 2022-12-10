"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument("com", help="operation name", type=str)
parser.add_argument("num1", help="Number1 to calculate", type=float)
parser.add_argument("num2", help="Number2 to calculate", nargs='?', type=float, default=0)


def calculate(com, num1, num2):
    try:
        return eval(f'{com}({num1})')
    except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
        try:
            return eval(f'math.{com}({num1})')
        except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
            try:
                return eval(f'operator.{com}({num1})')
            except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                try:
                    return eval(f'{com}({num1}, {num2})')
                except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                    try:
                        return eval(f'math.{com}({num1}, {num2})')
                    except (NotImplementedError, TypeError, AttributeError, NameError, ValueError):
                        try:
                            return eval(f'operator.{com}({num1}, {num2})')
                        except (NotImplementedError, TypeError, AttributeError, NameError, ValueError) as g:
                            raise g






def main():
    args = parser.parse_args()
    print(calculate(args.com, args.num1, args.num2))


if __name__ == '__main__':
    main()
