"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B """

#====================================================================================================================
sumBarang = int(input("Masukan Jumlah Barang: "))

#Memasukan nilai harga per barang ke dalam variabel
hargaA = 5000
hargaB = 4000
hargaC = 2500
hargaD = 3000

if sumBarang < 100:
    TotalA = sumBarang * hargaA # mencari total harga dengan operator kali 
    print(f"Total harga barang adalah {TotalA}") #print total harga 
elif 150>= sumBarang >= 100:
    TotalB = sumBarang * hargaB
    print(f"Total harga barang adalah {TotalB}")
elif sumBarang > 150:
    TotalC = sumBarang * hargaC
    print(f"Total harga barang adalah {TotalC}")

#==================================================================================================================


