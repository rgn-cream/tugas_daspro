"""Nama : Regina Nur Fadhilah 
Kelas : 1B 
NIM : 2406043"""

#Membuat dictionary baru yang menghitung berapa banyak siswa yang ada di setiap jurusan
students = {
    "Alice" : "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics"
}

a = list(students.values()).count("Computer Science")
print("prodi computer science sebanyak", a)

b = list(students.values()).count("Mathematics")
print("prodi mathematics sebanyak", b)

c = list(students.values()).count("Physics")
print("prodi physics sebanyak", c)
