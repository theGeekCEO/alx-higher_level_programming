#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for x in a:
        print("{}: {}".format(x, a_dictionary[x]))
