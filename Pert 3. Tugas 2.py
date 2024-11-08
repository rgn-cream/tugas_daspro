"""Nama : Regina Nur Fadhilah 
NIM : 2406043
Kelas : 1B"""

#=========================================================================================================================

"""Nomor 2: Diketahui tuple yang berisi daftar pasangan (latitude, longitude) sebuah lokasi sebagai berikut:
Jakarta: (-6.2088, 106.8456)
Bandung: (-6.9175, 107.6191)
Surabaya: (-7.2575, 112.7521)"""

#2a Tampilkan data koordinat untuk kota bandung===========================================================================

Jakarta = (-6.2088, 106.8456)
Bandung = (-6.9175, 107.6191)
Surabaya = (-7.2575, 112.7521)

print("Koordinat kota Bandung adalah:", Bandung) #Mencetak pasangan koordinat kota Bandung 
print("latitude:", Bandung[0], ", longitude:", Bandung[1]) #Mencetak koordinat kota Bandung 

#2b Tampilkan jumlah lokasi yang tersimpan================================================================================

Jakarta = (-6.2088, 106.8456)
Bandung = (-6.9175, 107.6191)
Surabaya = (-7.2575, 112.7521)

lokasi = (Jakarta, Bandung, Surabaya) #Menggabungan nama lokasi dalam satu tuple

print("Jumlah lokasi:", len(lokasi)) #Mencetak jumlah lokasi yang terdapat dalam tuple lokasi