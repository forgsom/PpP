#Дано целое число N (N > 0), являющееся некоторой степенью числа 3: N = 3K. Найти целое число K — показатель этой степени.


number = int( input("Enter number ") )
k = 0

while number > 1:
    k += 1
    number /= 3
print(k)
