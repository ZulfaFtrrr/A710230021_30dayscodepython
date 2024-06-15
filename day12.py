def hitung_kuadrat():
    while True:
        try:
            # Meminta input dari user
            bilangan = int(input("Masukkan bilangan bulat: "))

            # Menghitung kuadrat bilangan
            hasil = bilangan ** 2

            # Mencetak hasil kuadrat
            print("Hasil kuadrat dari", bilangan, "adalah:", hasil)

            # Keluar dari loop
            break
        except ValueError:
            # Menangani kesalahan jika input tidak valid
            print("Input yang dimasukkan tidak valid! Masukkan bilangan bulat.")

# Memanggil fungsi untuk menghitung kuadrat
hitung_kuadrat()