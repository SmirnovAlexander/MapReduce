#!/usr/bin/python

from functools import reduce

mapper = len

def reducer(item1, item2):
    """Compares lengths of two items.

    Returns longer item.
    """
    if item1[1] > item2[1]:
        return item1
    return item2

def find_longest_string_map_reduce(list_of_strings):

    # Step 1:
    mapped = map(mapper, list_of_strings)
    mapped = zip(list_of_strings, mapped)

    # Step 2:
    reduced = reduce(reducer, mapped)

    return reduced

list_of_strings = ['noSQL', 'python', 'parallel']
# list_of_strings = ['noSQL', 'python', 'parallel'] * 10000000
# list_of_strings = ['noSQL', 'python', 'parallel'] * 100000000

print(find_longest_string_map_reduce(list_of_strings))
