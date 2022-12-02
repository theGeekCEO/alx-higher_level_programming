#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    _len = len(args) - 1
    print("{} {}".format(_len, "arguments."
                               if _len == 0 else "argument:"
                               if _len == 1 else "arguments:"))
    for i in range(1, _len+1):
        print("{}: {}".format(i, args[i]))
