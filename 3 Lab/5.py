#Даны целые числа A и B (A < B). Вывести все целые числа от A до B включительно; при этом число A должно выводиться A раз, число A + 1 должно выводиться A + 1 раз и т. д.


A, B = int( input("A: ") ), int( input("B: ") )


for i in range(A, B+1):
    print()
    for j in range(A):
        print(A, end = ", ")
    A += 1
