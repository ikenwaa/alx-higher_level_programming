#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys = list(new_dict.key())

    for key in keys:
        new_dict[key] *= 2
    return new_dict
