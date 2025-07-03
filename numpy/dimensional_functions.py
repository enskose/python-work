import numpy as np

''' .shape: bir numpy dizisinin şeklini (boyutlarını) verir

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3)

# shape bir fonksiyon değildir, bir özelliktir. bu nedenle () kullanılmaz

'''

''' .flatten(): çok boyutlu bir diziyi tek boyutlu hale getirir (satır-sütun fark etmez, düzleştirir)

a = np.array([[1, 2], [3, 4]])
flat = a.flatten()
print(flat)  # [1 2 3 4]
'''

''' .reshape(): dizinin şeklini (boyutlarını) değiştirir ama eleman sayısı sabit kalır.

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)    # [[1 2 3]
            #  [4 5 6]]
'''





