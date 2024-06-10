def apakah_prima (bilangan_bulat):
     if bilangan_bulat > 1:
          for i in range (2,int(bilangan_bulat ** 0.5) + 1 ) :
               if (bilangan_bulat % i) == 0 :
                    return "bukan bilangan prima"
          else :
                 return " bilangan prima"
     else : return "bukan bilangan prima"

bilangan_bulat = int(input("masukan bilangan : "))
hasil = apakah_prima(bilangan_bulat)
print(hasil)