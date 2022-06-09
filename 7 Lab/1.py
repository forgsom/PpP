#Написать функцию с тремя параметрами, которая вычисляет наибольшее из заданных трех значений


def maxx(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a, b, c = int(input("A = ")), int(input("B = ")), int(input("C = ")),


print(maxx(a,b,c))
