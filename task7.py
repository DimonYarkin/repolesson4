from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


numStop = 0
for i in fibo_gen():
    if numStop < 15:
        print(i)
        numStop += 1
    else:
        break
