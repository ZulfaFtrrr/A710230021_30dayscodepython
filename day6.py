phone_book = {}

for l in range (5) :
     nama = input("masukan nama teman ke-{} :".format (l+1))
     no_hp =input("masukan nomor handphone temen ke-{} :".format(l+1))
     phone_book[nama] = no_hp

#menammpilkan(print/{})
print('-----------------------------------------------------------------')

print("phone_book".center(70))
for l,(nama,no_hp)in  enumerate(phone_book.items(),1) :
     print("{}.{} = {}".format(l,nama,no_hp))
     
print('------------------------------------------------------------------')