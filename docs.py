# syntax


# list (giong array):
li = [1, 2, 3]
li.pop() # drop last
li.append(4) # append to list
li[1:2:3] # get element in list by this formula: li[start, end, step]
del(li[2]) # remove by key
li.remove(2) # remove by key
li[2] = 2 # assign data to list, won't work with outranged key, ex: li[4] = 4
li.insert(4, 4) # insert to list by key, formula: insert(key, value)
1 in li # check if value in array
length = len(li) # check length
enumerate(li) # add index to list

# merge list:
li = [1, 2, 3]
li2 = [5, 6, 7]
li3 = li + li2 or li.extend(li2)

# tuple giong list, nhưng k sửa ddc element bên trong
tup = (1, 2, 3, 4, 5, 6)
tup1 = (7, 8, 9)
tup2 = tup + tup1

# dictionary:
dict1 = {'a': 1, 'b': 2}
dict2 = {('a', 'b') : [1, 2]}
dict1['a'] # or dict1.get('a')
dict1.get('c', 100) # default if not exists: 100
dict1['c'] = 3; # or dict1.update('c', 3)
dict1.setdefault('d', 4)
dict1.setdefault('d', 5) # d is still 4, because it's already set default
del(dict1['d'])
'a' in dict1
list(dict1.keys())
list(dict1.values())

#set
setempty = set()
set1 = {1, 1, 2, 2, 3, 3} # => set 2 = {1, 2, 3}, set loai bo nhung phan tu giong nhau
set1.add(4)
1 in set1
setcopy = set1.copy() # copy set
checkcopy = setcopy is set1 # tuy nhien setcopy van k phai la set1 => false
# lien ket set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
setgiongnhau = set1 & set2 # lay ra phan tu giong nhau cua ca 2 set => {3, 4}
setkethop = set1 | set2 # ket hop 2 set lai voi nhau => {1, 2, 3, 4, 5}
set1khacset2 = set1 - set2 # lay phan tu set 1 co ma set 2 ko co => {1, 2}
setkhacnhau = set1 ^ set2 # lay phan tu ca 2 set deu khong co cua nhau => {1, 2, 5}
#check cha con
set1 = {1, 2, 3}
set2 = {2, 3}
setcha = set1 >= set2 # check set 1 co la cha set 2 ko => true
setcon = set2 <= set1 # check set 2 co la con cua set 1 ko => true

# file handling
# open and write
file = open('/var/www/html/pythonlearning/test.py', 'w'); # or with open('/var/www/html/pythonlearning/test.py', 'w') as file2:
# w mean wrte
# r mean read
# w+ mean read and write. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# r+ mean read and write.
# write text to a file
file.write('this is a test')
# write json to a file
file3.write(str(dict1)) # write as a string
file3.write(json.dumps(dict1)) # write as a json
# read file
content4 = file4.read() # read a string file
content4 = json.load(file4) # read a json file


#function
def printArgs(*args): # *args tuc la truyen vo han bien nhung chi co value
def printKargs(**kargs): # **kargs tuc la truyen vo han bien nhung co key value
global a # bien global dat trong function se co the su dung o ngoai function
# function can be treated as variable
# lambda la 1 dang function co nhieu params, nhung chi tra ve 1 ket qua
y = (lambda x,y : x ** 2 + y ** 2)(2,3) # => 2^2 + 3^2 => 4 + 9 => 13

#class
# function trong class khi khai bao phai co self
def launch(self): # must have self
