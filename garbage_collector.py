# "circular references" example
# this is the error of python where a variable related to another variable and vice versa
# and python can't delete it and lead it to "memory leak"
# but "garbage collector" will handle it for us automatically
# so no need to worry about it
# and in this case, reference count won't be trustable

import ctypes
import gc
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Founded"
    return "Not Found"

class A:
    def __init__(self):
        self.b = B(self)
        print("A: {0}, b: {1}".format(id(self), id(self.b))) # result: B: 140402671469088, var_b: 140402671468704

class B:
    def __init__(self, obj):
        self.a = obj
        print("B: {0}, a: {1}".format(id(self), id(self.a))) # result: A: 140402671468704, var_a: 140402671469088

my_var = A()

gc.disable() # disable the garbage collector

a_id = id(my_var)
b_id = id(my_var.b)

print(object_by_id(a_id)) # result: Founded
print(object_by_id(b_id)) # result: Founded

print(ctypes.c_long.from_address(a_id).value) # result: 2, it's equal 2 because a reference to memory address and b reference to a
print(ctypes.c_long.from_address(b_id).value) # result: 1

my_var = None # unmark the my_var in memory

print(object_by_id(a_id)) # result: Founded
print(object_by_id(b_id)) # result: Founded

print(ctypes.c_long.from_address(id(a_id)).value) # result: 1
print(ctypes.c_long.from_address(id(b_id)).value) # result: 1

gc.collect() # enable the garbage collector

# because we have enable the garbage collector, so it will handle the circular references
print(object_by_id(a_id)) # result: Not Found
print(object_by_id(b_id)) # result: Not Found

# but the reference count is still return 1, so we can't trust on it
print(ctypes.c_long.from_address(id(a_id)).value) # result: 1
print(ctypes.c_long.from_address(id(b_id)).value) # result: 1