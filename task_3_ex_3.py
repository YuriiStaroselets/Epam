"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import fnmatch
import os
import stat



parser = argparse.ArgumentParser()
parser.add_argument("path", help="Absolute path for searching.", nargs="?", type=str)
parser.add_argument("-p", help="Can consist *, ?.", nargs="?", type=str)


def finder(path, pattern):
    find_el = []
    for file_path, _, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                find_el.append(os.path.join(file_path, file))
    return find_el

"""Searches for files by a given pattern.

:param path: Absolute path for searching.
:param pattern: Can consist *, ?.
:return: absolute path of found file.
"""




def display_result(find_el):
    """Displays founded file paths and file's permissions."""
    for el in find_el:
        premission = octal_to_string(el)
        print(el, premission)

    print(f"Found {len(find_el)} file(s).")







def octal_to_string(octal):
    result = ""
    mode = oct(stat.S_IMODE(os.lstat(octal).st_mode))[-3:]
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    for digit in [int(n) for n in str(mode)]:
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'
    return "-"+os.path.join(result)







def main():
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()