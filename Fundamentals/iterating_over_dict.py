# problemimiz: enes markette ne kadar harcadı
# price * quantity ile her ürünün toplam maliyetini bulacağız

# Ürünlerin fiyatlarını tutan sözlük (ürün adı: fiyat)


prices = {
    "box_of_spaghetti": 4,
    "lasagna": 5,
    "hamburger": 2
}

# Ürünlerin alınan miktarlarını tutan sözlük (ürün adı: miktar)
quantity = {
    "box_of_spaghetti": 6,
    "lasagna": 10,
    "hamburger": 0
}

# Toplam harcanan parayı tutacak değişkeni başlatıyoruz
money_spent = 0

# Her ürün için fiyat ve miktarı çarpıp toplam harcamaya ekliyoruz
for i in prices:
    # i: ürün adı, prices[i]: ürünün fiyatı, quantity[i]: alınan miktar
    money_spent = money_spent + (prices[i] * quantity[i])

# Sonuç olarak toplam harcanan parayı ekrana yazıyoruz
print(money_spent)



''' fiyatı 5 dolar ve üzeri olan ürünleri filtreleyip, Enes'in bu ürünler için ne kadar harcama yaptığını hesaplar

prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0

for i in prices:
    if prices[i] >= 5:
        money_spent = money_spent + (prices[i] * quantity[i])
    
print(money_spent)

'''    

