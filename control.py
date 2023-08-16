list1 = ['a', 'b', 'c']
for element in list1:
	print ("{} is an element in list".format(element))

for i in range(4):
	print (i) # => 1, 2 , 3, 4

for i in range(4, 8, 2): # range (lower, upper, step)
	print (i) # => 4, 6 . dunno why it's missing 8

for i, value in enumerate(list1): # add them index vao list
	print (i, value) # => 0 a 1 b 2 c

x = 0
while x < 4:
	print (x)
	x += 1