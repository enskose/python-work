# for döngüsü, bir iterable (yineleyebilir) nesne üzerinde yineleme yapmamızı sağlar.
# Bu iterable nesneler listeler, demetler (tuples), setler, sözlükler ve stringler gibi veri yapılarıdır.
# for döngüsü, belirli bir koşul sağlandığı sürece kod bloğunu tekrar tekrar çalıştırmamızı sağlar.
# for döngüsü, genellikle bir liste veya başka bir iterable üzerinde gezinmek için kullanılır.
'''
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

for number in even:
    print("Even Numbers:", even)
for number in odd:
    print("Odd Numbers:", odd)
'''

'''
for each value in sequence, perform action (bir dizideki her değer için bu eylemi gerçekleştirir)

for value in sequence: 
    action  
'''

# kurs örneği:

courses = {
    "LLM Concepts": "AI", 
    "Introduction to Data Pipelines": "Data Engineering", 
    "AI Ethics": "AI",
    "Introduction to dbt": "Data Engineering", 
    "Writing Efficient Python Code": "Programming",
    "Introduction to Docker": "Programming"
}

for key, value in courses.items():
  if value == "AI":
    print(key, "is an AI course")
  
  elif value == "Programming":
    print(key, "is a Programming course")
  
  else:
    print(key, "is a Data Engineering course")
  
  
  