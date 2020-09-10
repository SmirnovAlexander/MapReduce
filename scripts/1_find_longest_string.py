#!/usr/bin/python

def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0 
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string

# list_of_strings = ['noSQL', 'python', 'parallel']
# list_of_strings = ['noSQL', 'python', 'parallel'] * 10000000
list_of_strings = ['noSQL', 'python', 'parallel'] * 300000000

print(find_longest_string(list_of_strings))
