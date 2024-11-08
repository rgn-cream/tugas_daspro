"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B """

#======================================================================================
"""menghitung fungsi nilai total dan rata-rata berdasarkan input"""
#======================================================================================

def funArgs(*angka):
    total = sum(angka)
    average = total/len(angka)
    print(f"Total angka yang di input = {total}")
    print(f"rata-rata = {average}")
    return total,average

angka_list = [] 
while True :
    try :  
        angka = int(input("angka : "))
        angka_list.append(angka) 
    except ValueError: 
        break #berhenti saat user memaskan nilai yang bukan angka
    
funArgs(*angka_list)
print("Program selesai")




