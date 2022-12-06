#!/usr/bin/python3
def multiple_returns(sentence):
    len1 = len(sentence)
    f_char = "None" if len1 == 0 else sentence[0]
    return (len(sentence), f_char)
