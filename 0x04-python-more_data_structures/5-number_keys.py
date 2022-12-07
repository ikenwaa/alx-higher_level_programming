#!/usr/bin/python3
def number_keys(a_dictionary):
    dict_len = list(a_dictionary.keys())
    num = 0

    for i in dict_len:
        num += i
    return num
