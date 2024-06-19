class Orang:
    def __init__(self, nama, makanan_kesukaan, minuman_kesukaan, hobi):
        self.nama = nama
        self.makanan_kesukaan = makanan_kesukaan
        self.minuman_kesukaan = minuman_kesukaan
        self.hobi = hobi
    
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Hobi saya adalah {self.hobi}.")
        print(f"Saya suka makan {self.makanan_kesukaan}.")
        print(f"Minuman kesukaan saya adalah {self.minuman_kesukaan}.")

# Membuat objek untuk setiap orang
orang1 = Orang("Joni", "pizza", "kopi", "bersepeda")
orang2 = Orang("Jaja", "sushi", "teh", "membaca")

# Memanggil metode perkenalan untuk setiap objek
orang1.perkenalan()
print()  # Spasi antara perkenalan orang1 dan orang2
orang2.perkenalan()
