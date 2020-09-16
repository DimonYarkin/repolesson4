from random import random

my_list = [int(random() * 30) for el in range(30)]
print(f"Исходный список {my_list}")
list_new = [el for el in my_list if my_list.count(el) == 1]
print(f"Отобранный список {list_new}")
