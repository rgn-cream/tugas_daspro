"""Nama : Regina Nur Fadhilah
Kelas : 1B 
NIM : 2406043"""

#Data nama siswa, umur dan major/program studi 
student_info = {
    "Regina": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major":"Physics"}
}

nama_siswa = input("Inputkan nama siswa: ") #Memasukkan nama siswa yang akan ditampilkan
a = student_info.get(nama_siswa) #Mengakses item nama di dictionary student_info
age = a.get("age") #Mengakses data umur dari nama siswa yang di input
major = a.get("major") #Mengakses data major/program studi dari nama siswa yang di input 

print(f"Umur {nama_siswa} adalah {age} dan Prodinya adalah {major}")