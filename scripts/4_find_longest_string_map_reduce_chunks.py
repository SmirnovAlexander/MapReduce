#!/usr/bin/python

from functools import reduce
from math import ceil

mapper = len

def reducer(item1, item2):
    """Compares lengths of two items.

    Returns longer item.
    """
    if item1[1] > item2[1]:
        return item1
    return item2

def find_longest_string_map_reduce_chunks(list_of_strings, n_chunks=4):

    # Splitting data on chunks.
    step = ceil(len(list_of_strings) / n_chunks)
    data_chunks = [list_of_strings[x:x+step] for x in range(0, len(list_of_strings), step)]

    # Step 1:
    reduced_all = []
    for chunk in data_chunks:
        mapped_chunk = map(mapper, chunk)
        mapped_chunk = zip(chunk, mapped_chunk) 
        reduced_chunk = reduce(reducer, mapped_chunk)
        reduced_all.append(reduced_chunk)    

    # Step 2:
    reduced = reduce(reducer, reduced_all)

    return reduced

# list_of_strings = ['noSQL', 'python', 'parallel'] * 10
# list_of_strings = ['noSQL', 'python', 'parallel'] * 10000000
list_of_strings = ['noSQL', 'python', 'parallel'] * 100000000

print(find_longest_string_map_reduce_chunks(list_of_strings))
