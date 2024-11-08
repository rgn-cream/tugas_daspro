"""Nama : Regina Nur Fadhilah 
NIM : 2406043 
Kelas : 1B"""

"""Leni kembali menemui sebuah masalah baru. Kali ini dia ingin sekali mengetahui deret angka dari 1 sampai 50 dimana ketika bertemu dengan kelipatan 5 maka
outputnya adalah “pass”. Tolong bantu Leni dengan masalahnya kali ini."""
#=================================================================================================================

for i in range(1,51): #menentukan batasan range dari 1 sampai 50
    if i % 5 == 0 : #mengetahui kelipatan 5 dengan mencari modulus i 
        print("pass")
    else : 
        print(i)
