# Lists
# * Listeler, birden fazla veriyi sıralı ve değiştirilebilir şekilde saklamamıza yarayan yapılardır.
# * Listeler, köşeli parantezler [] ile tanımlanır ve elemanları virgülle ayrılır.
# * Listeler, farklı veri tiplerini içerebilir (sayılar, stringler, booleanlar vb.).


numbers = [10, 25, 30, 50]
# Listeler üzerinde çeşitli işlemler yapabiliriz:

# 1. Elemanlara erişim
print(numbers[0])  # 10
print(numbers[1])  # 25

# 2. Eleman ekleme
numbers.append(40)  # Listenin sonuna 40 ekler
print(numbers)  # [10, 25, 30, 50, 40]

# 3. Eleman silme
numbers.remove(30)  # 30 elemanını listeden siler
print(numbers)  # [10, 25, 50, 40]

# 4. Eleman güncelleme
numbers[1] = 35  # 25 elemanını 35 ile günceller
print(numbers)  # [10, 35, 50, 40]

# 5. Liste uzunluğu
print(len(numbers))  # 4

# 6. Listeyi sıralama
numbers.sort()  # Listeyi küçükten büyüğe sıralar
print(numbers)  # [10, 35, 40, 50]

# listeyi tersten sıralamak için 
numbers.sort(revers=True)
print(numbers)

# 7. Listeyi ters çevirme
numbers.reverse()  # Listeyi ters çevirir
print(numbers)  # [50, 40, 35, 10]

# 8. Listeyi temizleme
numbers.clear()  # Tüm elemanları siler
print(numbers)  # []

# 9. Listeyi kopyalama
numbers = [10, 25, 30, 50]
numbers_copy = numbers.copy()  # Listeyi kopyalar
print(numbers_copy)  # [10, 25, 30, 50]

# 10. Listeyi birleştirme
more_numbers = [60, 70]
numbers.extend(more_numbers)  # more_numbers listesini numbers listesine ekler
print(numbers)  # [10, 25, 30, 50, 60, 70]

# 11. Liste elemanlarını döngü ile gezme
for number in numbers:
    print(number)  # 10, 25, 30, 50, 60, 70

# 12. Sondan erişim (buradaki örnekte sondan üçüncü olana eriştik yani 25)
Numbers = [10, 25, 40, 50]
print(Numbers[-3])

# 13. list slicing (buradaki örnekte 1. indeksten 3. indekse kadar olanları aldık yani 25 ve 40)
print(Numbers[1:3])  # [25, 40]

# 14. numbers.index (buradaki örnekte 50 sayısının indeksi 3)
print(numbers.index(50))  # 3

# 15. iki listeyi birleştirerek daha büyük bir liste haline getirebiliriz
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesik_liste = [list1, list2]  # [1, 2, 3, 4, 5, 6]
print(birlesik_liste)  # [[1, 2, 3], [4, 5, 6]]

# 16. listedeki son 4 elemanı yazdırma
print(numbers[-4:])  # Son 4 elemanı yazdırır
