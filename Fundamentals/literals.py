# Değişkene atanabilecek herhangi bir sabit değer, literal / sabit değerler olarak adlandırılır.
# Constants: sabitler, bir programın yürütülmesi sırasında asla değişmeyen değerlerle ilişkili isimleri ifade eder.

integerNumber = 10 # bu bir constant değerdir yani sabit değerdir.
girdi = input("Bir değer giriniz: ") # b değişkeni ise sabit bir değer almamıştır, klavyeden herhangi bir değer girilebilir


# uzun basamaklı sayıları '_' alt çizgi ile ayırarak gösterebiliriz
x = 100_000_000 # böyle ayırarak yazarsak eğer okuması daha kolay olur 

'''
Literals
''' 
# float literals

f1 = 3.14 
f2 = 12E12
f3 = 12.5e-2

f4 = 125.67 # burada _ ile ayırma işlemi yapabiliriz, okunabilirliği arttırmamız gerekiyorsa 
            # fakat şunu yapamayız 5_._9 gibi bir kullanım mümkün değildir
            # _ 'ler sadece rakamlar arasında olmalıdır. Ondalıktan önce veya sonra kullanılamaz
            
# ______________________________________________________________________________________________________________ #
           
# boolean literals

a = True
b = False

# ______________________________________________________________________________________________________________ #

# complex literals

a = 4 + 5j
b = 12 + 14j # burada da _ kullanılabilir
c = 1.4 +   2.5j

# ______________________________________________________________________________________________________________ #

# string literals

# tek tırnak, çift tırnak ve üçlü tırnak şeklinde string ifadeler yazılabilir.
name = 'Enes'
name2 = "Enes"

# buradaki tek fark ekran çıktısı olacaktır, ekran çıktısı şu şekilde görünmektedir: "Enes"
name3 = '"Enes"'
print(name3)