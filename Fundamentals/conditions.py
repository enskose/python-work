# kullanıcıdan yaşını al ve 18'den küçükse reşit değil, büyükse reşit olduğunu yazdır
'''
age = int(input("Yaşınızı giriniz: "))
if age < 18:
    print("Reşit değilsiniz")

else:
    print("Reşitsiniz")

'''    

# _______________________________________________________________________________________________________________ #
'''    
num1 = int(input("Birinci sayıyı giriniz: "))
num2 = int(input("İkinci sayıyı giriniz: "))

if num1 > num2:
    print("Birinci sayı büyüktür ", num1, ">", num2)

elif num1 < num2:
    print("İkinci sayı büyüktür ", num2, ">", num1)

else:
    print("Her iki sayı eşittir ", num1, "=", num2)
    
# burada dikkat edilmesi gereken nokta, eğer if ve else if (elif) koşullarından hiçbiri sağlanmazsa else kısmı çalışır.

'''