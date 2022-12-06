#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_tup = (len(sentence), None)
    else:
        new_tup = (len(sentence), sentence[0])
    return new_tup
