li = [1, 2, 3]
li.pop()
li.append(4)
print (li)
print (li[2])

# li[start:end:step]
# li[::2] => cach 2 index thi lay phan tu.
# VD li = [1, 2, 3, 4]
# li[::2] => [1, 3]
li = [1, 2, 3, 4]
print (li[::2])

li = [1, 2, 3, 4]
del(li[2])
print(li)

li = [1, 2, 3, 4]
li.remove(2)
print(li)

li = [1, 2, 3, 4]
# insert (key, value)
li.insert(2, 1)
print(li)

li = [1, 2, 3, 4]
li2 = [5, 6, 7]
li3 = li + li2 # or li.extend(li2)
print(li3)

1 in li

print(li)
length = len(li) # check length
print (length)

li = [1, 2, 3]
# li[4] = 4 # throw error because there's no key 4 yet
li.insert(4, 4) # but this will work