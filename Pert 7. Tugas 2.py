"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B""" 

#==============================================================================================================

gender = input("Gender model (Wanita/Pria): ")
tb = float(input("Tinggi badan model (cm): "))
umur = int(input("Umur model: "))
iq = float(input("IQ model: "))


if gender.lower() == "wanita":
    if tb >= 170 and umur >= 18 and umur <=25 and iq >= 130:
        print("Anda dapat menjadi model catwalk")    
    else :
        print("Anda tidak memenuhi syarat sebagai model catwalk")

elif gender.lower() == "pria" :
    if tb >= 175 and umur >= 18 and umur <=25 and iq >= 130:
        print("Anda dapat menjadi model catwalk")    
    else :
        print("Anda tidak memenuhi syarat sebagai model catwalk")

print("Selamat anda menjadi model catwalk")

#================================================================================================================   

