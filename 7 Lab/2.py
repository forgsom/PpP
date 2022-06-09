#Написать функцию, вычисляющую наименьшее общее кратное.


def NOK(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


a, b = int(input("A = ")), int(input("B = "))


print(NOK(a, b))
