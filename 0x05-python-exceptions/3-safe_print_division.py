#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a/b
    except (ValueError, TypeError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(r), end="\n")
        return (r)
