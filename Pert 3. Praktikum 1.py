"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""


#No1 

a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
a[2] = "cherry"

print(a)

#No2 & 3

a = ["apel", "jeruk", "cherry", "durian", "apel", "mangga"]
x = input("index: ")
z = input("nilai: ")
a.insert(int(x),z)

print(a)
a.sort()
print(a)


