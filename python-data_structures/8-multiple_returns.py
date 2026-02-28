#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    first_char = sentence[0] if count > 0 else "None"
    tup = count, first_char
    return(tup)
