#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for b in my_string:
        if b == "c" or b == "C":
            a = a + ""
        else:
            a = a + b
    return (a)
