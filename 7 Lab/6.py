# Написать функцию, находящую максимум в одномерном массиве.
from random import randint


def maxx(arrar):
    max_ = arrar[0]
    for i in arrar:
        if i > max_:
            max_ = i
    return max_


a = []


for i in range(10):
    a.append(randint(-10, 10))

    
print(a)
print(maxx(a))
