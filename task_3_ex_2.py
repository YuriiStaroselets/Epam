import argparse

parser = argparse.ArgumentParser()
parser.add_argument("revs", help="string to calculate", nargs="?", type=str)


class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        if s == None:
            s = "GG"
        try:
            for i in s:
                if i not in rom_val:
                    raise ValueError()
                else:
                    for i in range(len(s)):
                        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                        else:
                            int_val += rom_val[s[i]]
                    return int_val
        except:
            raise ValueError()


def main():
    args = parser.parse_args()
    print(py_solution().roman_to_int(args.revs))



if __name__ == "__main__":
    main()