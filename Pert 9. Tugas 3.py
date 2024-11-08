"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas ; 1B"""

#====================================================================================================
"""Selisih waktu"""
#====================================================================================================

def selisih():
    print("Input mulai")
    jm = int(input("Jam = "))
    mm = int(input("Menit = "))
    dm = int(input("detik = "))

    print("\nInput Selesai")
    js = int(input("Jam = "))
    ms = int(input("Menit = "))
    ds = int(input("detik = "))
    
    #validasi jika waktu mulai lebih besar dari waktu selesai
    if (jm > js) or (jm == js and mm > ms) or (jm == js and mm == ms and dm > ds):
        print("\nWaktu mulai tidak boleh lebih besar dari waktu selesai")
        return  #jika waktu mulai lebih besar, langsung return dan tidak ada hasil yang dikembalikan
    
    selisihJam = js - jm
    selisihMenit = ms - mm
    selisihDetik = ds - dm 

    if selisihDetik < 0 : 
        #ketika selisih detik negatif, maka menit dikurangi 1 dan detik jadi 60. karena 60 detik = 1 menit
        selisihDetik += 60
        selisihMenit -= 1

    if selisihMenit < 0 :
        #ketika selisih menit negatif, maka jam dikurangi 1 dan menit jadi 60. karena 60 menit = 1 jam
        selisihMenit += 60 
        selisihJam -= 1 
    
    return selisihJam, selisihMenit, selisihDetik 

hasil = selisih()

#menampilkan hasil hanya jika hasil valid
if hasil: 
    print("\nMAka, selisih waktu =", hasil[0], "Jam -", hasil[1], "Menit -", hasil[2], "Detik")



