class Tiket:
  def __init__(self, jenis, jumlah):
    self.jenis = jenis
    self.jumlah = jumlah

  def harga(self):
    raise NotImplementedError("Method harga() harus diimplementasikan di subclass")

class TiketBiasa(Tiket):
  def harga(self):
    return self.jumlah * 30000

class TiketVIP(Tiket):
  def harga(self):
    return self.jumlah * 65000

class TiketGold(Tiket):
  def harga(self):
    return self.jumlah * 100000

def main():
  jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ")
  jumlah_tiket = int(input("Masukkan jumlah tiket: "))

  if jenis_tiket == "biasa":
    tiket = TiketBiasa(jenis_tiket, jumlah_tiket)
  elif jenis_tiket == "vip":
    tiket = TiketVIP(jenis_tiket, jumlah_tiket)
  elif jenis_tiket == "gold":
    tiket = TiketGold(jenis_tiket, jumlah_tiket)
  else:
    print("Jenis tiket tidak valid")
    return
  
  total_harga = tiket.harga()
  print(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == "__main__":
  main()
  