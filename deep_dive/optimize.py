"""
pre-calculate (difference based on python version)

python will pre-caculate for us the below cases, and that'll optimize the time:
- calculate number with constant number. Ex: 24 * 60. this is because 24 and 60 is constant number, it's not gonna change while we run the program
- short sequences length < 20. Ex: "abc" * 3 => 'abcabcabc' => less than 20 character
"""

def my_func():
    a = 24 * 60 # result: pre-calculated to 1440
    b = (1, 2) * 5 # result: pre-calculated to (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
    c = "abc" * 3 # result: pre-calculated to 'abcabcabc'
    d = "ab" * 11 # result: pre-calculated to 'ababababababababababab'
    e = "this is a long string" * 5 # result: NOT pre-calculated because it's longer than 20 character (with python > 3.8, this is no longer be the limit for string, but for other data type, it's still limited 20 character)

# this is function to check the pre-calculate items
print(my_func.__code__.co_consts) 
# result: 
# (
    # None, 
    # 1440, 
    # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2), 
    # 'abcabcabc', 
    # 'ababababababababababab', 
    # 'this is a long stringthis is a long stringthis is a long stringthis is a long stringthis is a long string'
# )


"""
membership test

in membership test, use `set` instead of other data type whenever you can, because it's way faster
"""

import string
import time

print(string.ascii_letters) # result: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('time calculate of list: ', end - start) # result: 2.19

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('time calculate of tuple: ', end - start) # result: 2.13

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('time calculate of set: ', end - start) # result: 0.22 => do membership test for set is way faster than list and tuple