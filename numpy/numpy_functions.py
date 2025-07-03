import numpy as np  

np_city = np.array([
    [1.73, 1.68, 1.71, 1.89, 1.79],
    [65.4, 59.2, 63.6, 88.4, 68.7]
])

''' .mean() fonksiyonu: elemanların ortalamasını hesaplar

np_city = np.array([[[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]]])  # 3 boyutlu bir numpy dizisi oluşturur (boy ve kilo verileri)

print(np.mean(np_city[:, 0]))  # dizinin ilk satırındaki (boy verileri) elemanların ortalamasını hesaplar

'''

''' .median(): medyan (veri serisini küçükten büyüğe doğru sıraladığımızda, bu serinin ortasında bulunan değerdir.)

print(np.median(np_city[:, 0])) # tüm kişileri küçükten büyüğe doğru sıralarsak bu sıralamanın ortasında olacak kişinin boyu (medyan)

'''

''' .corrcoef(): korelasyon (ne olduğunu tam anlayamadım gibi ama hayırlısı)
corr = np.corrcoef(np_city[0], np_city[1]) # Boy ve kilo verileri arasındaki korelasyon katsayısını hesaplar
print(corr)

'''

''' .std(): standart sapma

stds = np.std(np_city[:, 0])
print(stds)
'''

# sum(), sort() temel fonksiyonlar da bulunur

''' np.zeros(): tüm elemanları 0 olan bir NumPy dizisi oluşturur, sonrada içerisine istediğimiz değeri atayabileceğimiz bir numpy dizisi oluşturur.

print(np.zeros((5, 3))) # 5 satır ve 3 sütundan oluşan, tüm elemanları 0 olan bir NumPy dizisi oluşturur

'''

''' .axis(): işlemin hangi yönde yapılacağını belirtir

np_city = np.array([
    [1.73, 1.68, 1.71, 1.89, 1.79],  # boy
    [65.4, 59.2, 63.6, 88.4, 68.7]   # kilo
])

print(np.mean(np_city, axis=0))  # her sütunun ortalamasını alır [boy, kilo] kişiye özel ortalama
print(np.mean(np_city, axis=1))  # her satırın ortalamasını alır boyların ortalaması, kiloların ortalaması

# axis=0 sütunlar boyunca işlem yapılır (yukarıdan aşağıya)
# axis=1 satırlar boyunca işlem yapılır (soldan sağa)

'''

''' np.random.random(): 0 ile 1 arasında rastgele ondalıklı sayılar üretir.

# Tek bir rastgele sayı üretir
print(np.random.random())  # örnek çıktı: 0.73294847

# Belirli boyutta (örneğin 3x2) rastgele sayı matrisi oluşturur
print(np.random.random((3, 2)))
# çıktı:
# [[0.45 0.91]
#  [0.14 0.77]
#  [0.88 0.23]]

# Notlar:
# - Üretilen sayılar 0.0 ile 1.0 arasında (1 dahil değil)
# - Daha büyük sayılar için: np.random.random() * 100
# - Daha sonra tam sayıya çevirmek istersen: .astype(int) veya np.floor() kullanabilirsin

# Örnek: 5 elemanlı rastgele sayı dizisi oluşturma
rand_arr = np.random.random(5)
print(rand_arr)

# Örnek: 5 integer elemanlı rastgele sayı dizisi oluşturma
rand_arr = (np.random.random(5) * 100).astype(int)
print(rand_arr)

'''

''' np.arange(): Belirli bir başlangıç, bitiş ve adım değeri ile sayılardan oluşan bir NumPy dizisi oluşturur.

# Sadece bitiş değeri verildiğinde (başlangıç 0 kabul edilir):
print(np.arange(5))        # [0 1 2 3 4]

# Başlangıç ve bitiş verilir:
print(np.arange(2, 10))    # [2 3 4 5 6 7 8 9]

# Başlangıç, bitiş ve adım değeri verilir:
print(np.arange(1, 11, 2)) # [1 3 5 7 9]

# Ondalıklı sayılarla da çalışabilir:
print(np.arange(0, 1, 0.2))  # [0.  0.2 0.4 0.6 0.8]

# Not:
# - Bitiş değeri dahil değildir (tıpkı range() gibi)
# - Sonuç float ise dikkat: aralıklar çok hassas hesaplanır ve bazen küsurat farkı olabilir
'''

''' np.zeros(shape, dtype): Belirtilen boyutta, tüm elemanları 0 olan bir NumPy dizisi oluşturur.

zero_int_array = np.zeros((3, 2), dtype=np.int32)

Bu satır, 3 satır ve 2 sütundan oluşan bir NumPy dizisi oluşturur.
Tüm değerler sıfırdır ve veri tipi (dtype) int32 olarak belirlenmiştir.

print(zero_int_array)
# Çıktı:
# [[0 0]
#  [0 0]
#  [0 0]]

print(zero_int_array.dtype)  # int32

Notlar:
- dtype parametresi ile dizinin veri türü (int, float, bool, vb.) önceden ayarlanabilir.
- Varsayılan dtype → float64’tür (yani .0’lı ondalıklı değerler üretir).
- Bu yöntem, bellek yönetimi ve performans için önemlidir.
'''



