"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""

#=============================================================================================================================================

"""Nomor 1 : Diketahui list dengan nilai 10 mahasiswa sebagai berikut: 
88, 75, 63, 97, 82, 74, 91, 80, 81, 63"""

#1a menampilkan nilai maksimum, minimun, dan rata-rata =====================================================================================

#nilai maksimum
r = [70,71,90,99,88,90,23,66,87]
print(max(r)) #mencetak nilai maksimum dari list r

#nilai minimum
r = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
print(min(r)) #mencetak nilai minimum dari list r

#nilai rata-rata
r = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
average = float(sum(r))/(len(r)) #menjumlahkan nilai list r menggunakan sum() lalu dibagi dengan jumlah karakter pada list r menggunakan len()

print(average) #mencetak nilai rata-rata dari list r

#1b Menampilkan angka terbesar kedua dalam daftar nilai tersebut ====================================================================================
r = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
r.sort() #mengurutkan nilai dari yang terkecil

print(r) #mencetak list yang telah diurutkan
print(r[8]) #mencetak nilai terbesar kedua yang berada di index 8