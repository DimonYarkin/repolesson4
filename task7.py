from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


n = int(input("Введите количесво чисел для вывода: "))
numStop = 0
for i in fibo_gen():
    if numStop < n:
        print(i)
        numStop += 1
    else:
        break
