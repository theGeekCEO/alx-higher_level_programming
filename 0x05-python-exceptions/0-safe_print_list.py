#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return (i if i == 0 else i + 1)
    except IndexError:
        print()
        return (i)
