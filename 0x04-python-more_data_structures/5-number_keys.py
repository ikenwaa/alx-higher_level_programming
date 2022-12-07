#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0

    for i in range(len(a_dictionary.keys())):
        num += i
    return num
