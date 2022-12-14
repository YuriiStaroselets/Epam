""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("user_input", help="Number1 to calculate", type=str)


def check_formula(user_input, cache = []):
    if not cache:
        cache.append(user_input)
    if user_input and user_input[0].isdigit():
        user_input = user_input.lstrip('0123456789')
        if not user_input or user_input == ' ':
            return True, eval(cache[0])
        if user_input[0] in "+-":
            return check_formula(user_input[1:])
    return False, None


def main():
    args = parser.parse_args()
    print(check_formula(args.user_input))




if __name__ == '__main__':
    main()
