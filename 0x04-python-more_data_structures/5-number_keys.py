#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    dict_len = list(a_dictionary.keys())

    for i in dict_len:
        num += i
    return num
