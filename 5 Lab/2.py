#В одномерном массиве найти минимальный элемент с четным индексом


import random


a = []
min = 99999


for i in range(10):
    a.append(random.randint(-100, 100))


    if (i % 2 == 0) and min > a[i]:
        min = a[i]


print(a)
print(min)
