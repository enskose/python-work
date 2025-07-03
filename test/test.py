''' def dort_islem
def dort_islem(a, b, islem):
    if islem == "topla":
        return a + b
    elif islem == "cikar":
        return a - b
    elif islem == "carp":
        return a * b
    elif islem == "bol":
        if b == 0:
            raise ZeroDivisionError("Bölme işlemi için ikinci sayı sıfır olamaz.")
        return a / b
    else:
        raise ValueError("Geçersiz İşlem. Şunları Kullan: 'topla', 'cikar', 'carp', or 'bol'.")
print(dort_islem(999, 0, "bol"))

'''

''' list_numbers
Numbers = [15, 40, 50, 100, 115, 140]
Two_Numbers = [1, 2]
All_Numbers = [Numbers, Two_Numbers]
print(All_Numbers)
'''

''' def rectangle_area
def rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result = rectangle_area(5, 10)
print("Area:", result[0])
print("Perimeter:", result[1])
'''

''' dict dep_workers
dep_workers = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"],
    "Sales": ["Eve", "Frank"]
}

# ilk yazmış olduğumuz department " " arasına yazdığımız ünvanlar için,  ":" 'dan sonra atamış olduğumuz değerlere ise workers diyoruz.
# key:value ikilisi, yani burada "HR", "Engineering", "Sales" gibi departman isimleri anahtar (key) olarak kullanılırken, 
# bu departmanlardaki çalışan isimleri ise değer (value) olarak kullanılıyor.

# döngümüzde ise ilk başta key, value in dict ismi (dep_workers.items():) ile sözlüğün anahtar ve değerlerine erişiyoruz.
# Her bir departman için çalışanları listeleyip yazdırıyoruz.

for department, workers in dep_workers.items():
    print(f"{department} Departmanı Çalışanları:")
    for worker in workers:
        print(f"- {worker}")
    print()  
    
'''

''' dict departmants 
departments = {
    "HR": [
        {"name": "Alice", "age": 30, "position": "Recruiter"},
        {"name": "Bob", "age": 28, "position": "HR Manager"},
        {"name": "Charlie", "age": 32, "position": "Training Specialist"}
        ],
    "Engineering": [
        {"name": "David", "age": 35, "position": "Software Engineer"},
        {"name": "Eve", "age": 29, "position": "DevOps Engineer"}
        ],   
}

departments["HR"].append({"name": "Fiona", "age": 27, "position": "Compensation Analyst"})

for department, employees in departments.items():
    print(f"{department} Departmanı: ")
    for employee in employees:
        print(f"  - {employee['name']}, {employee['age']} yaşında, {employee['position']}")
    print()
    
departments["Engineering"] = [
    emp for emp in departments["Engineering"] if emp["name"] != "Eve"]
'''

''' dict Menu (udemy problem çözümü)
Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}
Price_list = {
    'Spaghetti': 10,
    'Fries': 5,
    'Cheeseburger': 8,
    'Lasagna': 12,
    'Soup': 5
}
print(Price_list)

'''

''' while döngüsü
x = 0
while x <= 29:
    x += 1
    if x % 2 == 1:
        print(x, end = " ")
        
'''

''' iki listeyi birleştirip sayma
x = [15, 10, 2, 84] + [1, 4, 8, 7, 9]
print(x.index(x.count(x[0])))
'''

''' 0'dan 10'a kadar olan sayılardan çift ve tek olanları etiketleme
for x in range(10):
    if x % 2 == 0:
        print(x, ("(Çift)"), end = " ")
    else:
        print(x, "(Tek)", end = " ")
'''
   
'''   
     
x = [0, 1, 2]

for item in range(len(x)):
    print(x[item], end = " ")

'''

''' 1'den 10 dahil, kadar olan tüm sayıları 2 ile çarpma
numbers = list(range(1, 11))

for num in numbers:
    print(num * 2)

'''

'''
n = [1,2,3,4,5,6]

for num in n:
    print(n * 2, end = " ")
    
for num in range(len(n)):
    print(n[num], end = " ")
    
'''

''' bir listede 20'den az olan sayıları sayma
def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
    return total

ex_list = [1, 2, 3, 45, 76, 88, 12]

print(count(ex_list))
'''

''' liste üzerinde while döngüsü ile gezinerek, 20’den küçük sayıların sayısını döndürür.
nums = [1,35,12,24,31,51,70,100]

def count(nums):
    i = 0
    x = 0
    while i < len(nums):
        if nums[i] < 20:
            x += 1
        i += 1
    return x

print(count(nums))
'''



