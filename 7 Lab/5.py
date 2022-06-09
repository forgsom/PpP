#Написать функцию, которая переводит число из десятичной системы счисления в двоичную или восьмеричную.



def change(x, i):
    b = ""
    while x > 0:
        b = str(x%i) + b
        x = x // i
    print(b)


x = int(input("x = "))

change(x, 2)
change(x, 8)
