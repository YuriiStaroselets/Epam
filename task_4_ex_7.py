"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""

from typing import List


def product_array(num_list: List[int]) -> List[int]:
    for i in num_list:
        if type(i) != int:
            raise NotImplementedError
    res = []
    for i in num_list:
        sumno = 1
        for a in num_list:
            if a != i:
                sumno *= a
        res.append(sumno)
    return res
