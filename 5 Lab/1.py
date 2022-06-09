#В одномерном массиве, содержащем положительные и отрицательные целые числа, вычислить сумму нечетных отрицательных элементов.


import random


a = []
sum = 0


for i in range(10):
    a.append(random.randint(-10, 10))


    if (a[i] % 2 != 0) and (a[i] < 0) :
        sum += a[i]


print(a)
print(sum)
