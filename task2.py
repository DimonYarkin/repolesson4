from random import random

my_list = [int(random() * 300) for el in range(20)]
print(f"Исходный список {my_list}")
list_new = [my_list[i] for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]
print(f"Отобранный список: {list_new}")
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
