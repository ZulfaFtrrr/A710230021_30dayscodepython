prodi = 'Pendidikan Teknik Informatika'
nama_depan=input('Masukan Nama Depan    : ')
nama_belakang=input('Masukan Nama Belakang : ')
nama_lengkap="".join([nama_depan, nama_belakang])

nim='A710230021'

fakultas='Fakultas Keguruan dan Ilmu pendidikan'

univ='Universitas Muhammadiyah Surakarta'
kapital=univ.upper()
#print 
print('------------------------------------------------------------------')
print(prodi.center(70))
print('NAMA   :'+nama_lengkap)
print('NIM    : {}'.format(nim))
print(fakultas)
print(kapital.center(70))
print('------------------------------------------------------------------')