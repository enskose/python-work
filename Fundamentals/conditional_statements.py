
# if - else - elif 
'''
x = int(input("1. Sayı: "))
y = int(input("2. Sayı: ")) 

if x > y:
    print(f"{x} > {y}")

elif x < y:
    print(f"{x} < {y}")

else:
    print(f"{x} = {y}")

'''

# fonksiyon kullanarak yazdığım biraz daha gelişmiş bir örnek


y = int(input("Bir sayı giriniz: "))

def compare_to_five(y):
    if y > 5:
        return f"{y} > 5"
    elif y < 5:
        return f"{y} < 5"
    else:
        return f"{y} = 5"
    
print(compare_to_five(y))