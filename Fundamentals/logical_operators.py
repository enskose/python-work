# Logical and Identity Operators

# not - and - or - is
# 'and' ve 'or' operatörleri boolean değerler döndürür

# 'and' iki durumunda doğruluğunu kontrol eder
x = 10
print(x > 5 and x < 20)  #! True çünkü her iki koşul da doğru


# 'or' iki durumdan birinin doğruluğunu kontrol eder
x = 3
print(x < 2 or x == 3)  #! True çünkü ikinci koşul doğru


# 'not' bir durumun tersini alır
is_active = False
print(not is_active)  #! True çünkü is_active False


# 'is' iki nesnenin aynı olup olmadığını kontrol eder
a = [1, 2, 3]
b = a
print(a is b)  #! True çünkü aynı liste nesnesine işaret ediyorlar


# 'is not' iki nesnenin aynı olmadığını kontrol eder
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)  #! True çünkü içerik aynı ama nesneler farklı

        
        