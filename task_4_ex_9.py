"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    if type(n) != int:
        raise TypeError()
    if n<0:
        raise TypeError()

    resls = [int(digit) for digit in str(n)]
    res = 0
    for i in resls:
        if i % 2 != 0:
            res += i
    return res
