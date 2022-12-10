"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(s: str) -> str:
  dict = { '"':"'", "'":'"' }
  return ''.join(dict.get(c, c) for c in s)
