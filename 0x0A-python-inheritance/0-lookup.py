#!/usr/bin/python3
'''0. Lookup
Return list of available attributes and methods
of an object.
'''


def lookup(obj):
    '''Return list of object's available attributes.'''
    return dir(obj)
