#!/usr/bin/python

def find_longest_string_steps(list_of_strings):

    # Step 1:
    list_of_string_lens = [len(s) for s in list_of_strings]
    list_of_string_lens = zip(list_of_strings, list_of_string_lens)

    # Step 2:
    max_len = max(list_of_string_lens, key=lambda t: t[1])

    return max_len

list_of_strings = ['noSQL', 'python', 'parallel']
# list_of_strings = ['noSQL', 'python', 'parallel'] * 10000000
# list_of_strings = ['noSQL', 'python', 'parallel'] * 100000000

print(find_longest_string_steps(list_of_strings))
