#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = list.copy(my_list)
    lnt = len(my_list)
    if idx < 0 or idx >= lnt:
        return (a)
    a[idx] = element
    return (a)
