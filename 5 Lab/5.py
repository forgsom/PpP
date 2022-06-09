#Определить, какое число в массиве встречается чаще всего.



import random


a = []
b = []
k = 0
max = -20

for i in range(10):
    a.append(random.randint(-10, 10))


for i in range(10):
    for j in range(10):
        if a[i] == a[j]:
            k += 1
    b.append(k)
    k = 0

    if b[i] > max:
        max = b[i]
        index = i



print(a)
print(a[index])
