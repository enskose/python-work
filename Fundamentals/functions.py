# Fonksiyonlar, kodu tekrar tekrar yazmamak için kullanılır.

# "def" yazarak fonksiyon oluşturuyoruz.
# Fonksiyonlara istersek dışarıdan bilgi (parametre) verebiliriz.
# Fonksiyonlar bazen bize bir sonuç (return) döndürebilir.
'''
def fonksiyon_adi(parametre1, parametre2):
    # Burada fonksiyonun yapmasını istediğimiz işlemleri yazıyoruz
    return parametre1 + parametre2

# Fonksiyonu çağırırken adını ve gerekli bilgileri yazıyoruz:
sonuc = fonksiyon_adi(3, 5)
print(sonuc)  # Burada ekrana 8 yazdırılır

'''

'''
def exponentiation_exp_2(x):
    result = x ** 2
    print("Raised to the power of 2:", result)
    return result

exponentiation_exp_2(5)
'''

'''

# Fonksiyonlar, kodu daha düzenli ve tekrar kullanılabilir hale getirir.
def wage(w_hours):
    return w_hours * 20

def bonus(w_hours):
    return wage(w_hours) + 50

print("Wage for 8 hours:", wage(8), "Bonus:", bonus(8))

'''
# _________________________________________________________________________________________________ *# 

'''
def plus_five(x):
    return x + 5

def m_by_3(y):
    return plus_five(y) * 3

result = m_by_3(5)
print(result)  

'''

# Fonksiyonlarda if-else yapısı kullanma
'''
def add_10(m):
    if m >= 100:
        m += 10
        print("Bonus added! New amount:", m)
    else:
        print("Save more money to get a bonus.")

add_10(50)

'''

# Birden fazla parametreye sahip fonksiyonlar
'''
def subtract_bc(a, b, c):
    result = a - b * c
    print("Paramter b equals:", a)
    print("Paramter a equals:", b)
    print("Paramter c equals:", c)
    print("Result of subtraction:", result)
    return result

subtract_bc(10, 3, 2)
'''

# built-in fonksiyonlar

# Create a function, called distance_from_zero(), that returns the absolute value of a provided 
# single argument and prints a statement "Not possible" if the argument provided is not a number. To solve the task, 
# use the type() function in the body of distance_from_zero().
# Call the function with the values of -10 and "cat" to verify it works correctly. 

def distance_from_zero(arg):
    if type(arg) == int:
        return abs(arg)
    else:
        print("Not possible")

print(distance_from_zero(-10))   
print(distance_from_zero("cat")) 
