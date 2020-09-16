from random import random

my_list = [int(random() * 300) for el in range(20)]
print(f"Исходный список {my_list}")
list_new = [my_list[i] for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]
print(f"Отобранный список: {list_new}")
