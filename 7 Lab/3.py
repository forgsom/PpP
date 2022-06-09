#Написать функцию, которая выводит вашу фамилию на экран указанное количество раз.


def repeat_name(name, number):
    for i in range(number):
        print(name, end=" ")


name = input("KAK TEBYA ZOVUT ")
number = int(input("number = "))


repeat_name(name, number)
