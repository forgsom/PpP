#Дано целое число N (N > 0). Найти наименьшее целое положительное число K, куб которого превосходит N: K 3 > N. Функцию извлечения квадратного корня не использовать.


number = int( input("Enter number ") )
k = 1


while k * k * k <= number:
    k += 1


print(k)
