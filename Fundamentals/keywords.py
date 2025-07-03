# in = bir değerin bir değişkende/veri yapısında olup olmadığını (if) kontrol etmemizi sağlar

products_dict = {
    "AG32": 10,
    "HT91": 20,
    "PL61": 30,
    "0S31": 15,
    "KB07": 25,
    "TR48": 35
}

if "0S31" in products_dict.keys():
    print(True)
else:
    print(False)
    
# not = bir koşulun gerçekleşmediğini kontrol etmek için kullanılır

if "HT91" not in products_dict.keys():
    print(False) # "HT91" product kütüphanemizde bulunmuyorsa bunu çalıştır
else:
    print(True) # bulunuyorsa bunu (yukarıdakinin yani "in" anahtar kelimesinin yaptığı işlemin tam tersini yapar)
    

# and = birden fazla koşulun sağlanıp sağlanmadığını kontrol etmemizi sağlar

if "KB07" and "AG32" in products_dict.keys():  
    print(True)  # kontrol etmek istediğimiz key'lerin ikisi de bulunuyorsa True,
else:
    print(False) # ikisinden birisi veya ikisi de yoksa False çalışır
    

if "HT91" in products_dict.keys() and min(products_dict.values()) > 5:
    print(True)
else:
    print(False)
    

# or = birden fazla koşul sağlamamız ve en az 1 bir tanesinin doğru olup olmadığını değerlendirmemize yardımcı olur 

if "AG32" in products_dict.keys() or "HT91" in products_dict.keys() and min(products_dict.values()) > 19:
    print(True)
else:
    print(False)
    
    
# belirli şartları karşılayan bilgileri depolamak için bir liste kullanmak istediğimizi varsayalım.
# örneğin en az 20 dolar değerindeki tüm ürünlerin ürün kimliklerini gibi kriterlere sahip bir liste

expensive_products = []

for key, val in products_dict.items():
    if val > 20:
        expensive_products.append(key)
        
print(expensive_products)

