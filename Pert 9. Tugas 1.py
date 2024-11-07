"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B""" 

#=============================================================================================
"""Deret Fibonacci menggunakan fungsi sebanyak N dari user input """
#=============================================================================================

def fibonacci(n):
    bil1 = 0 
    bil2 = 1 
    for i in range(n):
        print(bil1, end=" ")
        bil1, bil2 = bil2, bil1 + bil2

jumlah_deret = int(input("Masukkan banyak bilangan fibonacci yang ingin di tampilkan = "))
fibonacci(jumlah_deret)