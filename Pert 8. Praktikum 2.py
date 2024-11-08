"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B """

#LATIHAN 2 =======================================================================================================
#Buatlah sebuah program yang meminta pengguna memasukkan angka-angka berturut-turut. Program akan menghitung total angka yang dimasukkan pengguna hingga pengguna memasukkan angka negatif.

jumlah = 0 #jumlah awal adalah 0

a = float(input("Masukkan angka: ")) #input angka 

while a >= 0:
    jumlah += a #menambahkan variabel jumlah dengan a
    a = float(input("Masukkan angka: ")) #input ulang angka

print(f"Total dari angka positif yang di input = {jumlah}")

