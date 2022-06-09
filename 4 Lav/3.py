#Дано целое число N (N > 0). Используя операции деления нацело и взятия остатка от деления, найти число, полученное при прочтении числа N справа налево.


number = int( input("Enter number ") )

while number > 0:
    tempNumber = number % 10
    number = number // 10
    print(tempNumber, end = "")
