# lien ket set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
setgiongnhau = set1 & set2 # lay ra phan tu giong nhau cua ca 2 set => {3, 4}
setkethop = set1 | set2 # ket hop 2 set lai voi nhau => {1, 2, 3, 4, 5}
set1khacset2 = set1 - set2 # lay phan tu set 1 co ma set 2 ko co => {1, 2}
setkhacnhau = set1 ^ set2 # lay phan tu ca 2 set deu khong co cua nhau => {1, 2, 5}

print (setgiongnhau)
print (setkethop)
print (set1khacset2)
print (setkhacnhau)

setcopy = set1.copy()
checkcopy = setcopy is set1
print(setcopy)
print(checkcopy)