"""
Create function sum_geometric_elements, determining the sum of the first elements of a decreasing geometric
progression of real numbers with a given initial element of a progression `a` and a given progression step `t`,
while the last element must be greater than a given `lim`. `an` is calculated by the formula (an+1 = an * t), 0<t<1
Function must return float and round the answer to three decimal places using round().
Check the parameter `t` and raise a ValueError if it does not satisfy the inequality 0<t<1.
`a` and `lim` must be greater than 0, otherwise raise a ValueError.

Example,
For a progression, where a1 = 100, and t = 0.5, the sum of the first elements, grater than alim = 20, equals to
100+50+25 = 175
"""


def sum_geometric_elements(a: float, t: float, lim: float) -> float:
    if a < 0 or lim < 0:
        raise ValueError
    if 0<t<1:
        x = 0
        res = a
        el = a
        while x != 1:
            el *= t
            if el > lim:
                res += el
            else:
                break
        return round(res)
    else:
        raise ValueError
