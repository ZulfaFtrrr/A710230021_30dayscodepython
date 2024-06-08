tahun_lahir = int(input('Masukan Tahun Lahir :'))
harga_tiket = int(input('masukan harga_Tiket :'))

usia = int(2023) - int(tahun_lahir)

if(usia >= 0 and usia <=4):
    diskon = harga_tiket*(100/100)
    setelah_diskon = harga_tiket - diskon
    print("karena usia 0-4 Mendapatkan Diskon 50%, Total Harganya Yaitu :",setelah_diskon)

elif(usia >= 5 and usia <= 11):
    diskon = harga_tiket *(50/100)
    setelah_diskon = + harga_tiket - diskon
    print("Karena usia 5-11 mendapatkan Diskon 50%,Total harganya yaitu :",setelah_diskon)

else :
    print("karena Tidak Mendapatkan Diskon Dikarenakan Usia Sudah Diatas 11 tahun")