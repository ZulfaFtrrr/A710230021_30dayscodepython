class Mahasiswa:
     def __init__(self,nim,nama,angkatan,prodi) :
          self.nim = nim
          self.nama = nama
          self.angkatan = angkatan
          self.prodi = prodi

     def kartu_mahasiswa(self) :
          print(f"Data Mahasiswa\nNIM : {self.nim}\nNama : {self.nama}\nAngkatan : {self.angkatan}\nProdi : {self.prodi}\n")

     def selamat(self) :
          print(f"Selamat Datang {self.nama} di Kampus UMS")

#objek objek Mahasiswa
mahasiswaA = Mahasiswa("A71020001", "Aprilia Mustika",2020,"Pendidikan Matematika")
mahasiswaB = Mahasiswa("A71023455","Nadia Aulia",2023,"Pendidikan Teknik Informatika")
mahasiswaC = Mahasiswa("B51018005","Muhammad Risky",2018,"Teknik Informatika")

#Memanggil method Kartu_mahasiswa dan Selamat
mahasiswaA.kartu_mahasiswa()
mahasiswaA.selamat()
print("\n")

mahasiswaB.kartu_mahasiswa()
mahasiswaB.selamat()
print("\n")

mahasiswaC.kartu_mahasiswa()
mahasiswaC.selamat()
print("\n")
