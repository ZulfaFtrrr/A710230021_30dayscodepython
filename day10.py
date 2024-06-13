# Definisi class Orang
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

# Definisi class Mahasiswa yang merupakan turunan dari class Orang
class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")

# Definisi class Pekerja yang merupakan turunan dari class Orang
class Pekerja(Orang):
    def __init__(self, nama, umur, tempatKerja):
        super().__init__(nama, umur)
        self.tempatKerja = tempatKerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatKerja}")

# Membuat objek dari masing-masing kelas
orang = Orang("Salsabila", 19)
mahasiswa = Mahasiswa("Zulfa Fitri Delafani", 20, "Universitas Muhammadiyah Surakarta")
pekerja = Pekerja("Navilla", 19, "PT Jaya Abadi")

# Memanggil method kenalan untuk setiap objek
orang.kenalan()        
mahasiswa.kenalan()   
pekerja.kenalan()  
