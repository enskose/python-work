import pandas as pd
import numpy as np


''' pd.Series(): pandas kütüphanesinin 1D veri yapısıdır.

Temel özellikleri:
- Liste, NumPy array, dict gibi yapılardan oluşturulabilir
- Otomatik indeksleme yapar veya kullanıcı tanımlı index kabul eder

Örnek:
import pandas as pd

s = pd.Series([10, 20, 30])
# 0    10
# 1    20
# 2    30

s2 = pd.Series([85, 90, 95], index=["Math", "Physics", "Chemistry"])
# Math        85
# Physics     90
# Chemistry   95

Notlar:
- s[0] → 10
- s["Math"] → 85
- Series, DataFrame’in yapı taşıdır (DataFrame = birden fazla Series)
'''

# pandas versiyon kontrolü: print(pd.__version__)

products = ['A', 'B', 'C', 'D']

# listeyi series'e dönüştürmek istersek

product_categories = pd.Series(products) # index=[3, 5, 7, 9]) yazarak da custom indeksleme yapabiliriz
print(product_categories)
print(type(pd.Series(products))) # <class 'pandas.core.series.Series'>


daily_rates_dollars = pd.Series([40, 45, 50, 60])
print(daily_rates_dollars)

array_a = np.array([10, 20, 30, 40, 50])
print(type(array_a)) # <class 'numpy.ndarray'>

series_a = pd.Series(array_a)
print(series_a)

print(type(series_a))

# Pandas Series nesnesi, Python listesinin güçlü bir versiyonu veya numpy dizisinin geliştirilmiş bir versiyonu gibidir.

# Her zaman veri tutarlılığını korumayı unutma. (verilerin tek veri tipine sahip olması)

