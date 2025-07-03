import numpy as np

# örnek bir 2D NumPy dizisi
array_2 = np.array([
    [4, 5],
    [7, 10]
])

"""
numpy'da 'axis' kavramı, işlemin hangi yönde yapılacağını belirtir.

   [[ 4,  5],
    [ 7, 10]]

   Shape (2, 2)
   Yani 2 satır ve 2 sütunluk bir matris.
"""

# -----------------------------------------------
# Axis = 0 → Sütunlar boyunca işlem yapılır (dikey)
# Yani her sütundaki elemanlar birlikte işlenir.
# Bu durumda → Yukarıdan Aşağıya işlem yapılır.

column_mean = np.mean(array_2, axis=0)  # [ (4+7)/2 , (5+10)/2 ] → [5.5, 7.5]
print("Sütun ortalamaları (axis=0):", column_mean)


# -----------------------------------------------
# Axis = 1 → Satırlar boyunca işlem yapılır (yatay)
# Yani her satırdaki elemanlar birlikte işlenir.
# Bu durumda → Soldan Sağa işlem yapılır.

row_mean = np.mean(array_2, axis=1)  # [ (4+5)/2 , (7+10)/2 ] → [4.5, 8.5]
print("Satır ortalamaları (axis=1):", row_mean)


# -----------------------------------------------
# Axis belirtilmezse → tüm elemanların ortalaması alınır

overall_mean = np.mean(array_2)  # (4+5+7+10)/4 → 6.5
print("Tüm elemanların ortalaması:", overall_mean)


"""
Özet:

- axis=0 → sütunlar boyunca işlem (dikey ↓)
- axis=1 → satırlar boyunca işlem (yatay →)
- axis belirtilmez → tüm dizi üzerinde işlem yapılır

Bu kural np.sum(), np.max(), np.std(), np.min(), vb. fonksiyonlar için de geçerlidir.
"""
