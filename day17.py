# Definisi kelas Orang
class Orang:
    def __init__(self, nama, umur):  # Corrected __init__ method
        self.nama = nama
        self.umur = umur

    def perkenalkan_diri(self):
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

# Definisi kelas Mahasiswa yang mewarisi dari kelas Orang
class Mahasiswa(Orang):
    def __init__(self, nama, umur, jurusan):  # Corrected __init__ method
        super().__init__(nama, umur)  # Corrected call to super().__init__
        self._jurusan = jurusan

    @property
    def jurusan(self):
        return self._jurusan

    @jurusan.setter
    def jurusan(self, value):
        self._jurusan = value

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Zulfa Fitri", 19, "Pendidikan Teknik Informatika")

# Mengakses properti jurusan sebelum diubah
print(f"Jurusan sebelum: {mahasiswa1.jurusan}")

# Mengubah nilai properti jurusan
mahasiswa1.jurusan = "Akuntasi"

# Mengakses properti jurusan setelah diubah
print(f"Jurusan setelah: {mahasiswa1.jurusan}")

# Memperkenalkan diri
mahasiswa1.perkenalkan_diri()
