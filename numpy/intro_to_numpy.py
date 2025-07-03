import numpy as np

''' boy ve kilo listelerinden numpy dizileri oluşturulup BMI hesaplanıyor.
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)

print("23'ten büyük boy mass index:", bmi[bmi > 23])

np.array([True, 1, 2]) + np.array([3, 4, False])
'''

''' 2 boyutlu numpy dizisi üzerinde indeksleme ve slicing işlemleri yapılıyor.
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape) # ekran çıktısı (2, 5) # sol taraf (2) satır, sağ taraf (5) sütun 2x5'lik bir matrix

print(np_2d[0][2]) # subsetting

print(np_2d[:, 1:3]) # tüm satırlardan, 2. ve 3. sütunları (yani index 1 ve 2'yi) seçip ekrana yazdırır. 
                     # çok boyutlu dizilerde belirli sütunları kolayca çekmek için kullanılır.
print(np_2d[1, :]) # sadece kilo bilgilerinin verir yani index 1'in tamamını verir. eğer bu 0 olsaydı boy bilgisini verirdi yani index 0'ı

'''

''' bir beyzbol veri seti üzerinde toplama ve çarpma işlemleri uygulanıyor.
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

'''

