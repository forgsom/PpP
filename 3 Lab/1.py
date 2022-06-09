# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые
# числа, расположенные между A и B (не включая числа A и B), а также количество
# N этих чисел.


first_number, second_number = int( input("Enter first number ") ), int( input("Enter second number ") )
k = 0

for i in range(second_number-1, first_number, -1):
    k += 1
    print(i)

print("KOLLICHESTVO =", k)
