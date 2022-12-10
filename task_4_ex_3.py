"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=" ") -> list:
    list = []
    pos = -1
    last_pos = -len(delimiter)
    if type(str_to_split) == str:
        if type(delimiter) == str:
            while delimiter in str_to_split[pos + len(delimiter):]:
                pos = str_to_split.index(delimiter, pos + len(delimiter))
                list.append(str_to_split[last_pos + len(delimiter):pos])
                last_pos = pos
            list.append(str_to_split[last_pos + len(delimiter):])
        else:
            raise ValueError()
    else:
        raise ValueError()
    return list
