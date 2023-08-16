print(2 + 5)

if (5 < 2) :
	print ('case 1')
else :
	print ('case 2')

print (True + 5) # True = 1
print (False + 5) # False = 0

#round là làm tròn, sẽ lấy giá trị int gần nhất, nếu âm thì sẽ lấy xuống 1 đơn vị.
print (5 // 3) # round => 1
print (-5 // 3) # round => -2

#chia hết và trả về số dư:
print (7 % 3); # => 1
print (-7 % 3); # => 2

# ^ changed to **
print (2 ** 3)

a = "case 1" if 1 > 0 else "case 2"
print (a)

x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x # gan value x = y va y = x, kieu nhu swap value
print (x, y, z)