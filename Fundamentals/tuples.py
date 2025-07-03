tuple_example = (1, 2, 3, 4, 5)
# Tuples, Python'da değiştirilemez (immutable) veri tipleridir ve köşeli parantezler yerine normal parantezler () ile tanımlanır.

# Accessing elements in a tuple
first_element = tuple_example[0]

# Slicing a tuple
slice_example = tuple_example[1:4]  # This will give (2, 3, 4)

# Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = tuple_example + another_tuple  # This will give (1, 2, 3, 4, 5, 6, 7, 8)

# Repeating tuples
repeated_tuple = tuple_example * 2  # This will give (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Bu fonksiyon, verilen uzunluk ve genişlik 
# ile bir dikdörtgenin alanını ve çevresini hesaplayıp tuple olarak döndürür.

def rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

result = rectangle_area(5, 10)
print("Area:", result[0])
print("Perimeter:", result[1])
