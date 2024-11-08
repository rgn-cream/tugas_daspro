"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""

#==========================================================================================================================
# Menentukan terlebih dahulu apakah bilangan input positif atau negatif, lalu dicek ganjl atau genap

bil = float(input("Masukkan bilangan bulat: "))

if (bil>0): 
    bil_positif= "positif"
    if (bil% 2==0):
        print(f"bilangan {bil} adalah {bil_positif} dan termasuk bilangan genap")
    else:
        print(f"bilangan {bil} adalah {bil_positif} dan termasuk bilangan ganjil")
elif (bil<0):
    bil_negatif = "negatif"
    if (bil% 2==0):
        print(f"bilangan {bil} adalah {bil_negatif} dan termasuk bilangan genap")
    else:
        print(f"bilangan {bil} adalah {bil_negatif} dan termasuk bilangan ganjil")

else:
    print(f"bilangan {bil} adalah nol")

#======================================================================================================================

