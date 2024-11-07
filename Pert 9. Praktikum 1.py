"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""
#=======================================================================================
"""Menghitung volume tabung menggunakan fungsi"""
#=======================================================================================

def voltabung (r,t):
    #rumus volume tabung = phi * r^2 * t
    a = r**2
    b = t
    v_tabung = 3.14 *a * b
    print(f"Volume tabung = {v_tabung}")
    return v_tabung

voltabung(2,3)

