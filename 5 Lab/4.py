#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.



import random


a = []
max = 0
min = 9999


for i in range(10):
    a.append(random.randint(-100, 100))
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
print(a)


for i in range(10):
    for j in range(10):
        if a[i] == max and a[j] == min:
            a[i], a[j] = a[j], a[i]


print(a)
