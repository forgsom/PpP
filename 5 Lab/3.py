#Найти номер максимального по модулю элемента массива


import random


a = []
max = 0


for i in range(10):
    a.append(random.randint(-100, 100))


    if abs(a[i]) > max:
        max = abs(a[i])
        k = i


print(a)
print(k)
