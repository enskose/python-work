import numpy as np

# 2 boyutlu bir NumPy dizisi (matrix) oluşturalım
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]]) 

# arr[0, 1] ifadesi: 0. satır, 1. sütundaki elemana erişir (sonuç: 2)
print(arr[0, 1])

# arr[2, :] ifadesi: 2. satırdaki tüm elemanlara erişir (sonuç: [7 8 9])
print(arr[2, :])

# arr[:, 0] ifadesi: tüm satırlardaki 0. sütun elemanlarına erişir (sonuç: [1 4 7])
print(arr[:, 0])

# arr[1:3, 1:3] ifadesi: 1. ve 2. satır, 1. ve 2. sütunlardan oluşan alt matrise erişir (sonuç: [[5 6], [8 9]])
print(arr[1:3, 1:3])

''' slicing with steps: liste veya dizi içinde belirli aralıklarla eleman seçmeyi sağlar.

Söz dizimi: sequence[start:stop:step]

# Örnekler:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[::2])     # [0 2 4 6 8] 2’şer adım
print(arr[1:8:3])   # [1 4 7] 1. indexten başla, 3’er adım ilerle
print(arr[::-1])    # [9 8 7 6 5 4 3 2 1 0] ters çevirme
'''

''' np.sort(): bir numpy dizisini küçükten büyüğe sıralar ve sıralanmış yeni bir dizi döndürür.

arr = np.array([5, 1, 3])
sorted_arr = np.sort(arr)
print(sorted_arr)  # [1 3 5]

# 2D dizilerde:
array_name = np.array([[8, 4, 2],
                   [7, 9, 1]])

print(np.sort(array_name, axis = 0))  # sütun sütun sırala
print(np.sort(array_name, axis = 1))  # satır satır sırala

Notlar:
- Orijinal array değişmez, kopya döner.
- axis = 0 sütunlar boyunca sıralama
- axis = 1 satırlar boyunca sıralama
'''


