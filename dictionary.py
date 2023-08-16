dict1 = {'a': 1, 'b': 2}
print (dict1)

dict2 = {('a', 'b') : [1, 2]}
print (dict2)

print (dict1['a'])

print (dict1.get('a'))
print (dict1.get('c', 100)) # default if not exists: 100

a = list(dict1.keys())
print (a)

b = list(dict1.values())
print (b)

'a' in dict1

dict1['c'] = 3; # or dict1.update('c', 3)
print (dict1)

dict1.setdefault('d', 4)
dict1.setdefault('d', 5) # d is still 4, because it's already set default
print (dict1)

del(dict1['d'])
print (dict1)
