#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    _len = len(my_list)
    if idx < 0 or idx >= _len:
        return my_list
    del my_list[idx]
    return (my_list)
