#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        freq = 0

        for tup in my_list:
            (weight, tally) = tup
            total += (weight * tally)
            freq += tally
        return (total/freq) if freq > 0 else 0
    else:
        return 0
