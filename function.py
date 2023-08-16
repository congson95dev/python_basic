# normal function
def tinhtong(x, y):
	print("x is {} and y is {}".format(x, y))
	return x + y

tong = tinhtong(4, 5)
print ('result is: {}'.format(tong))


# *args tuc la truyen vo han bien nhung chi co value
def printArgs(*args):
	for arg in args:
		print(arg)

printArgs('This', 'is', 'a', 'test') # khong co key


# **kargs tuc la truyen vo han bien nhung co key value
def printKargs(**kargs):
	for key, value in kargs.items(): # chu y kargs phai co .items(), args ben tren k co
		print("key is {} and value is {}".format(key, value))

printKargs(a = 'This', b = 'is', c = 'a', d = 'test') # co key va value

# global variable
x = 10
def test():
	x = 100
	global y # bien global se su dung duoc o ngoai function
	y = 200

test()
print(x) # x still = 10
print(y) # y = 200

# function can be treated as variable
def create_adder(x):
	def adder(y):
		return x + y
	return adder

add_10 = create_adder(10)
add_3 = add_10(3)
print(add_3) # => 13

# filter() and map()
ages = [5, 12, 17, 18, 24, 32, 24]

def myFunc(age):
	if age > 18:
		return str(age) + ' > 18'
	else:
		return False

result = filter(myFunc, ages)
for age in result:
	print (age)
# result:
'''
24
32
24
'''

result = map(myFunc, ages)
for x in result:
	print(x)
# result:
'''
False
False
False
False
24 > 18
32 > 18
24 > 18
'''

# lambda la 1 dang function co nhieu params, nhung chi tra ve 1 ket qua
x = lambda a : a + 10
print(x(5)) # => 15

y = (lambda x,y : x ** 2 + y ** 2)(2,3)
print(y) # => 2^2 + 3^2 => 4 + 9 => 13

# goi function trong 1 function khac
a = list(map(add_10, [1, 2, 3])) # chay add_10 voi tung so 1, 2, 3
print(a) # => [11, 12, 13]

b = list(map(max, [1, 2, 3], [3, 2, 1])) # lay max cua tung row cua 2 array.
print(b) # => [3, 2, 3]


