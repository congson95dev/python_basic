import numpy as np

"""
array
"""
my_list = [1, 2, 3, 4]
print(type(my_list))  # result: list
my_arr = np.array(my_list)
print(type(my_arr))  # result: numpy.ndarray

my_2d_list = [
    [1, 2, 3],
    [4, 5, 6]
]
my_2d_arr = np.array(my_2d_list)
print(my_2d_arr)
print(my_2d_arr.ndim)  # result: 2 => same as result when using len() function
print(my_2d_arr.shape)  # result: (2, 3)

"""
arange
"""
a = np.arange(0, 10)
print(a)  # result: [0 1 2 3 4 5 6 7 8 9], ignore 10
b = np.arange(0, 10, 2)
print(b)  # result: [0 2 4 6 8], ignore 10

"""
common function
"""
# with this example: [0 1 2 3 4 5 6 7 8 9]
print(a.max())  # result: 9
print(a.min())   # result: 0
print(a.mean())  # result: 4.5, get average

# with this example: [[1 2 3], [4 5 6]]
print(my_2d_arr.sum())  # result: 21
print(my_2d_arr.sum(axis=1))
# result: [6, 15],
# because it only caculate sum of each row
print(my_2d_arr.sum(axis=0))
# resukt: [5 7 9],
# because it only calculate sum of each column


"""
compare
"""
print(a > 5)  # result: [False False False False False False  True  True  True  True]
print(a[a > 5])  # result: [6 7 8 9]

"""
access to data inside array
"""
# with this example: [0 1 2 3 4 5 6 7 8 9]
print(a[0])  # result: 0
print(a[-1])  # result: 9
print(a[4:8])  # result: [4, 5, 6, 7], ignore 8
print(a[:8])  # result: [0 1 2 3 4 5 6 7], ignore 8
print(a[5:])  # result: [5 6 7 8 9]

"""
access to data inside array (multi dimension)
"""
# with this example: [[1, 2, 3], [4, 5, 6]]
print(my_2d_arr[0])  # result: [1, 2, 3]
print(my_2d_arr[0][2])  # result: 3
print(my_2d_arr[0, 2])  # result: 3, same as above but with difference way to write code
print(my_2d_arr[:, 1:])  # result: [[2 3], [5 6]]

"""
change data inside array
"""
a[5:] = 99  # replace all the data
print(a)  # result: [ 0  1  2  3  4 99 99 99 99 99]

"""
reshape
"""
c = a.reshape(2, 5)
print(c)  # result: [[0 1 2 3 4], [5 6 7 8 9]]

"""
operation
it will affect to every element inside the array
"""
a = np.arange(0, 10)
print(a + 5)
print(a - 5)
print(a * 5)
print(a / 5)

"""
random
"""
a = np.random.rand(5, 2)
print(a)
# result: create array with 5 rows and 2 columns
# with value is random float number from 0 -> 1
# Ex:
# [[0.6738453  0.86631995]
#  [0.58120185 0.55811754]
#  [0.58068512 0.94114053]
#  [0.57992641 0.424434  ]
#  [0.50227346 0.79506903]]

a = np.random.randint(0, 10, (5, 2))
print(a)
# result: create array with 5 rows and 2 columns
# with value is random integer number from 0 -> 9, ignore 10
# Ex:
# [[3 4]
#  [0 5]
#  [5 3]
#  [3 7]
#  [6 3]]
