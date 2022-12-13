#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = 0
    if not a_dictionary:
        pass
    else:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                best_key = key
    return best_key
