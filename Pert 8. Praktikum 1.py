"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""

#Buatlah program dengan looping sebanyak n = 10, setelah itu hitung jumlah dari angka tersebut.

n = 10 #nilai awal
jumlah = 0 #jumlah awal 

for index in range(0,n+2): # index dimulai dari 0 
    jumlah += index #variabel jumlah ditambahkan index
    print(f"saat index {index}, jumlah angka sementara {jumlah} " )

print (f"Total penjumlahan semua angka hasil perulangan {jumlah}")

