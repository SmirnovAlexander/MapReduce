#!/usr/bin/python

from functools import reduce
from math import ceil
from multiprocessing import Pool

mapper = len

def reducer(item1, item2):
    """Compares lengths of two items.

    Returns longer item.
    """
    if item1[1] > item2[1]:
        return item1
    return item2

def chunks_mapper(chunk):
    """Finding longest string in a chunk.
    """
    mapped_chunk = map(mapper, chunk) 
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)

def find_longest_string_parallel(list_of_strings, n_chunks=10):

    # Splitting data on chunks.
    step = ceil(len(list_of_strings) / n_chunks)
    data_chunks = [list_of_strings[x:x+step] for x in range(0, len(list_of_strings), step)]

    print("Finished splitting data")

    # Step 1:
    mapped = Pool().map(chunks_mapper, data_chunks)

    # Step 2:
    reduced = reduce(reducer, mapped)

    return reduced

# list_of_strings = ['noSQL', 'python', 'parallel'] * 3 
# list_of_strings = ['noSQL', 'python', 'parallel'] * 10000000
list_of_strings = ['noSQL', 'python', 'parallel'] * 100000000

print(find_longest_string_parallel(list_of_strings))
