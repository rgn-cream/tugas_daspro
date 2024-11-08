"""Nama : Regina Nur Fadhilah
NIM : 2406043
Kelas : 1B"""

#=====================================================================================================
"""Login dengan kesempatan 5 kali"""
#=====================================================================================================

def login():
    print("Silahkan Login")

    kesempatan = 5

    for i in range(kesempatan):
        username = input("Username : ")
        password = input("Password : ")

        pw = "Latihan"

        if password == pw :
            print (f"Halo {username}, anda berhasil login")
            break 
        
        else :
            kesempatan -= 1
            if kesempatan == 0 :
                print("Password salah! Kesempatan anda habis\n")
                print ("Anda tidak dapat mengakses aplikasi ini")
                break
            else : 
                print(f"Password anda salah! Kesempatan anda tersisa {kesempatan} kali lagi\n")
           
login()


