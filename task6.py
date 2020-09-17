from itertools import count, cycle

numStop = int(input("Введите сколько чисел необходимо сгенерировать? "))

for num in count(int(input("введите стартовое число: "))):
    print(f"сгенерированное число: {num}")
    if num >= numStop:
        break

my_list = [1, True, "Hi1"]
numStop = int(input("Введите сколько элементов необходимо сгенерировать? "))
i = 0
for el in cycle(my_list):
    print(el)
    i += 1
    if i >= numStop:
        break
