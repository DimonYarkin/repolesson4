from functools import reduce


def fuctr(arg1, arg2):
    return arg1 * arg2


my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(f"Сгенерированный список {my_list}")

print(f"Результат умножения {reduce(fuctr, [el for el in my_list])}")
