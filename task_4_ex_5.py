"""Implement a function `get_digits(args: int) -> Tuple[int]` which receives
arbitrary amount of arguments and returns a tuple of digits of given integers.

Example:
```python
>>> split_by_index(8717, 82911, 99)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""


def get_digits(*args):
    L1 = list(args)
    res = tuple()
    for i in L1:
        l1=[int(digit) for digit in str(i)]
        res += tuple(l1)
    return res
