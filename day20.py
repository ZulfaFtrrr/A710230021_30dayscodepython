class Karyawan:
    def __init__(self, nama, id_karyawan, jabatan, gaji):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.jabatan = jabatan
        self.gaji = gaji

    def get_info(self):
        return {
            'nama': self.nama,
            'id_karyawan': self.id_karyawan,
            'jabatan': self.jabatan,
            'gaji': self.gaji
        }
class Perusahaan:
    def __init__(self, nama_perusahaan):
        self.nama_perusahaan = nama_perusahaan
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        for karyawan in self.daftar_karyawan:
            info = karyawan.get_info()
            print(f"Nama       : {info['nama']}")
            print(f"ID         : {info['id_karyawan']}")
            print(f"Jabatan    : {info['jabatan']}")
            print(f"Gaji       : {info['gaji']}")
            print('-' * 20)
# Buat perusahaan
perusahaan_saya = Perusahaan("Perusahaan XYZ")

# Buat beberapa karyawan
karyawan_1 = Karyawan("Yaya", 1, "Manajer", 10000000)
karyawan_2 = Karyawan("Cika", 2, "Staf", 5000000)
karyawan_3 = Karyawan("Caca", 3, "Supervisor", 7000000)

# Tambah karyawan ke perusahaan
perusahaan_saya.tambah_karyawan(karyawan_1)
perusahaan_saya.tambah_karyawan(karyawan_2)
perusahaan_saya.tambah_karyawan(karyawan_3)

# Tampilkan daftar karyawan di perusahaan
print("Daftar Karyawan di Perusahaan:")
perusahaan_saya.tampilkan_karyawan()
