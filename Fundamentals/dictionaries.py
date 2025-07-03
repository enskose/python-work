# Dictionaries, Python'da anahtar-değer çiftlerini saklamak için kullanılır.

# Dictionaries, köşeli parantezler {} ile tanımlanır ve anahtarlar benzersiz olmalıdır.
dictionary_example = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Accessing elements in a dictionary
name = dictionary_example["name"]

# Sözlüğe yeni bir anahtar-değer çifti ekleme
dictionary_example["job"] = "Engineer"

# Var olan bir anahtar-değer çiftini güncelleme
dictionary_example["age"] = 31

# Bir anahtar-değer çiftini silme
del dictionary_example["city"]

# Anahtarlar ve değerler üzerinde döngü ile gezinme
for key, value in dictionary_example.items():
    print(f"{key}: {value}")
    
# Bir anahtarın sözlükte olup olmadığını kontrol etme
if "name" in dictionary_example:
    print("Name exists in the dictionary.")
    
# Varsayılan bir değer ile bir anahtarın değerini alma
age = dictionary_example.get("age", "Not Found")
print("Age:", age)

dict = {
    "name": "Enes",
    "Age": 24,
    "Fav Animal": "Cat",
}

dict["Fav Color"] = "Blue"  # Yeni anahtar-değer çifti ekleme
print("Güncellenmiş Dictionary:", dict)

# bir anahtara birden fazla değer atama
dict["Fav Numbers"] = [1, 2, 3, 4, 5]  # Liste olarak değer ekleme

# Sözlükteki tüm anahtarları ve değerleri listeleme
for key in dict:
    print(f"{key}: {dict[key]}")
    

# Bu sözlükte:
# - Anahtarlar (key): Departman isimleridir ("HR", "Engineering", "Sales").
# - Değerler (value): Her departmana ait çalışanların adlarını tutan liste yapılarıdır.

dep_workers = {
    "HR": ["Alice", "Bob"],
    "Engineering": ["Charlie", "David"],
    "Sales": ["Eve", "Frank"]
}


# Sözlüklerde her bir öğe "key: value" şeklinde tanımlanır.
# Burada her departman bir key, ona karşılık gelen çalışanlar da bir listedir (value).

# Aşağıdaki döngü ile:
# - Sözlüğün her bir anahtar-değer (key-value) çifti üzerinde geziniriz.
# - Her departmanın çalışanlarını yazdırırız.

for department, workers in dep_workers.items():
    print(f"{department} Departmanı Çalışanları:")
    for worker in workers:
        print(f"- {worker}")
    print()

# Not: Eğer çalışanlara ait yaş, pozisyon gibi bilgiler de tutulmak istenirse,
# liste yerine sözlük kullanmak daha esnek olur (nested dictionary).

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

departments["HR"].append({"name": "Fiona", "age": 27, "position": "Compensation Analyst"}) # HR departmanına yeni bir çalışan ekleme

# Bu kod, her departmanın çalışanlarını ve bilgilerini yazdırır.
for department, employees in departments.items():
    print(f"{department} Departmanı: ")
    for employee in employees:
        print(f"  - {employee['name']}, {employee['age']} yaşında, {employee['position']}")
    print()
    
# Engineering departmanından "Eve" adlı çalışanı silme
# Bu işlem, "Eve" adlı çalışanın adını kontrol ederek, eğer varsa o çalışanı listeden çıkarır.    
departments["Engineering"] = [
    emp for emp in departments["Engineering"] if emp["name"] != "Eve"]

# Udemy'den almış olduğum eğitimde sorulan sorunun cevabı: 
Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}
Price_list = {
    'Spaghetti': 10,
    'Fries': 5,
    'Cheeseburger': 8,
    'Lasagna': 12,
    'Soup': 5
}
print(Price_list)

# Menüdeki öğelere fiyat eklemek için, Price_list sözlüğünü kullanabiliriz.
# Her bir öğenin fiyatını, öğenin adını anahtar olarak kullanarak Price_list sözlüğüne ekleyebiliriz.
# Fiyatları yazdırmak için, Menu sözlüğündeki her bir öğeyi Price_list sözlüğünde arayabiliriz.
# Eğer öğe Price_list sözlüğünde varsa, fiyatını yazdırırız; yoksa "fiyat bulunamadı" mesajı veririz.
for meal_key, meal_name in Menu.items():
    if meal_name in Price_list:
        print(f"{meal_name} fiyatı: {Price_list[meal_name]}")
    else:
        print(f"{meal_name} için fiyat bulunamadı.")