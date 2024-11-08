"""Nama : Regina Nur Fadhilah 
Kelas : 1B
NIM : 2406043"""

#Menghapus semua duplikasi dan mengembalikan daftar angka yang hanya berisi elemen unik
numbers = [10,20,20,30,40,50,50,60]
elemen_unik = list(set(numbers)) 
print(elemen_unik)

#Mengurutkan elemen unik dari list yang sudah dihapus duplikasinya
numbers = [10,20,20,30,40,50,50,60]
elemen_unik = list(set(numbers)) 
elemen_unik.sort() #mengurutkan list
print(elemen_unik)

numbers2 = [11,12,13,14,15,19,22,25]
elemen_unik = list(set(numbers)) 
elemen_unik.sort() #mengurutkan list
print(elemen_unik)