#Даны целые числа 𝑎, 𝑏, 𝑐, являющиеся сторонами некоторого треугольника. Проверить, является ли треугольник со сторонами 𝑎, 𝑏, 𝑐 равнобедренным.


a, b, c = int(input("Enter first number\n")), int(input("Enter second number\n")), int(input("Enter third number\n"))


if (a == b) or (a == c) or (b == c):
    print("Yes")

else:
    print("No")
