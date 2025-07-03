
'''
Dikdörtgenin alanı:
# dikdörtgenin alanını bulmak için uzunluk ve genişlik çarpılır.
# alan = uzunKenar * kısaKenar

length = int(input("Uzun Kenar: "))
width = int(input("Kısa Kenar: "))

print("Uzun Kenar:", length, " Kısa Kenar:", width, " Alan:", length * width)

'''

'''
Üçgenin alanı:
# ucgenArea = (base * height) / 2

base = int(input("Taban: "))
height = int(input("Yükseklik: "))

print("Taban:", base, " Yükseklik:", height, " Alan:", (base * height) / 2)

'''

'''
Yamuk alanı:
# trapezArea = ((base1 + base2) * height) / 2

base1 = int(input("Taban 1: "))
base2 = int(input("Taban 2: "))
height = int(input("Yükseklik: "))

print("Taban 1:", base1, " Taban 2:", base2, " Yükseklik:", height, " Alan:", ((base1 + base2) * height) / 2)

'''

'''
import math 
(normalde kütüphaneleri ilk satırda import ederiz ama şu anda bu kütüphaneyi kullanmayacağız 
ve hata vermesin diye bu satırı yorum satırı haline getirdik.)

Daire alanı:
# circleArea = pi * radius ** 2
# burada pi sayısını kendimiz tanımlayabiliriz ama python'da math modülünde pi sayısı tanımlı olduğu için onu da deneyelim.

#pi = 3.14 (math kütüphanesini kullanmazsak pi sayısını kendimiz tanımlayabiliriz ama bu durumda pi sayısının tam değerini kullanamayız.)
radius = int(input("Yarıçap: "))
print("Yarıçap:", radius, " Alan:", math.pi * radius ** 2)


'''


''' burada bir alan hesaplamasından ziyade km'yi mile çevirme işlemi yapacağız.
# 1 km = 0.621371 mile
# 1 mile = 1.60934 km

km = int(input("Kilometre: "))
mile = km * 0.621371

print("Kilometre:", km, " Mile:", mile)

'''

'''
# displacement 
# displacement = finalPosition - initialPosition

u = int(input("Başlangıç Pozisyonu: "))
v = int(input("Bitiş Pozisyonu: "))
a = int(input("Hız: "))
d = (v*v - u*u) / (2*a)
print("Displacement:", d)

'''