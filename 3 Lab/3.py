#Дано вещественное число A и целое число N (N > 0). Используя один цикл, найти сумму:
# 2**0 - 2**1 + 2**2 - 2**3 = 1 - 2 + 4 - 8 = -5


number = float( input("Enter number ") )
N = int( input("N = ") )
summ = 0


for i in range(0, N+1):
    summ += ( number**i ) * ( (-1)**i )

print("Sum =", summ)
