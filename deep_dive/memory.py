"""
variable reference to a memory slot
using id() will show out the memory slot that the variable is referenced
"""
a = 10
print(id(a)) # print memory slot, result: 9793376
print(hex(id(a))) # print memory slot in hex version, result: 0x956f60

a = [1, 2, 3]

# sys.getrefcount() will always assign 1 reference count to the object when we called it
# so it will +1 to the result
# we need to -1 in our head whenever we call this function
import sys
print(sys.getrefcount(a)) # result: 2

# we have another way to count the reference, which will return the correct number
import ctypes
print(ctypes.c_long.from_address(id(a)).value) # result: 1

b = a
print(ctypes.c_long.from_address(id(a)).value) # result: 2
print(ctypes.c_long.from_address(id(b)).value) # result: 2

"""
re-assign
"""

a = 100
print(hex(id(a))) # result: 0x957aa0

# if we re-assign like this, the memory address will be changed too
a = a + 10
print(hex(id(a))) # result: 0x957be0

# this also happen to other data type as well, such as list, tuple
t = (1, 2)
print(hex(id(t))) # result: 0x7fbb26938e80
t = t + (3, 4)
print(hex(id(t))) # result: 0x7fae645de270

"""
mutable, immutable
"""

a = 100
print(hex(id(a))) # result: 0x957aa0
print(hex(id(100))) # result: 0x957aa0, this is the same as above, because the number is immutable so it already exists inside memory address list

# same thing happen to tuple because it's mutable
t = (1, 2)
print(hex(id(t))) # result: 0x7f3028a2be80
print(hex(id((1, 2)))) # result: 0x7f3028a2be80

a = [1, 2, 3]
print(hex(id(a))) # result: 0x7fd0ae4ef8c0
print(hex(id([1, 2, 3]))) # result: 0x7fd0ae50a980, this is difference as above, because the list is mutable so it doesn't exists already in memory address list

# even when we change the data of mutable variable, the memory address still remain the same.
a = [1, 2, 3]
print(hex(id(a))) # result: 0x7f6dea9d9a00
a.append(4)
print(hex(id(a))) # result: 0x7f6dea9d9a00

"""
side effect
mutable data type will have side effect
immutable data type will not have side effect
"""

# mutable data type will have side effect
def change_list(list_a) :
    list_a.append(4)

a = [1, 2, 3]
change_list(a)
print(a) # result: [1, 2, 3, 4], this is because list is mutable, so the `a` and `list_a` share the same memory address, so when we change the `list_a`, the `a` variable is also affected, this is side effect

# immutable data type will not have side effect
def change_string(string_a) :
    string_a += ' world'

a = 'hello'
change_string(a)
print(a) # result: 'hello', this is because string is immutable, so `a` and `string_a` (after we do string_a += ' world') is having difference memory address, so whenever we change the `string_a`, it won't affect to `a`

"""
string intern
"""

# a and b have the same memory address
a = 'hello'
b = 'hello'

# a and b will have difference memory address, because it's have "space" so python won't consider it as identify variable
a = 'hello world'
b = 'hello world'

# a and b have the same memory address because we force it to intern by using sys.intern()
import sys
a = sys.intern('hello world')
b = sys.intern('hello world')