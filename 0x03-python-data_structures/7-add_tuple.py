#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    a += 0 if len1 < 1 else tuple_a[0]
    a += 0 if len2 < 1 else tuple_b[0]
    b += 0 if len1 < 2 else tuple_a[1]
    b += 0 if len2 < 2 else tuple_b[1]

    return a, b
