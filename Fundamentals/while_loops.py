# while döngüsü, koşul sağlandığı sürece kodun sürekli çalışmasını sağlar ve 
# genellikle tekrar eden işlemler veya kullanıcıdan sürekli veri almak için kullanılır.


''' verilen cevaba göre sonsuz döngüde sürekli olarak dört işlem yapan, basit hesap makinesi 

while True:    
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    islem = input("İşlem Seçiniz (+, -, *, /):")
    
    if islem == "+":
        print("Toplama işleminin sonucu:", (sayi1 + sayi2))
    elif islem == "-":
        print("Toplama işleminin sonucu:", (sayi1 - sayi2))
    elif islem == "*":
        print("Toplama işleminin sonucu:", (sayi1 * sayi2))
    elif islem == "/":
        print("Toplama işleminin sonucu:", (sayi1 / sayi2))
    else:
        print("Geçersiz İşlem")
    
    cevap = input("İşlem yapmaya devam etmek ister misiniz? (evet için 'e', hayır için 'h')")
    if cevap == "e":
        continue
    elif cevap == "h":
        break
    else:
        print("Cevabınızı 'e' veya 'h' olarak belirtmelisiniz")
'''

# Koşula bağlı while döngüsü (conditional while loop), belirli bir şart sağlandığı sürece kod bloğunun tekrar tekrar çalışmasını sağlar. 

# satmış olduğumuz ürünün çıkış tarihine yakınlaştıkça yani tarih 24 olduğunda deneme sürümünün yayınlandığı bildirilsin, 
# tarih 25 olduğunda "yarın yayınlanıyor" vb. bir bildiri çıktı versin

release_date = 26
current_date = 22

while current_date <= release_date:
    
    current_date += 1
    
    if current_date <= 24:
        print(current_date, "Purchase before the 25th for early access")    
    elif current_date == 25:
        print(current_date, "Coming soon!")
    else:
        print(current_date, "Available now!")
    
    if current_date >= 26: # gün 26'yı geçtiğinde döngünün durması için
        break
    
