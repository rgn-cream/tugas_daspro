"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""


#No1 

a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah1 = a[3] = "cherry"
buah2 = a[2] = "mangga"

print(buah1, buah2)

#No2 & 3

a = ["apel", "jeruk", "cherry", "durian", "apel", "mangga"]
x = input("index: ")
z = input("nilai: ")
a.insert(int(x),z)

print(a)
a.sort()
print(a)


