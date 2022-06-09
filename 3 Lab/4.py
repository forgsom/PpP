#Дано целое число N (N > 1). Последовательность вещественных чисел AK определяется следующим образом:


N = int( input("Enter N ") )
if N == 0:
    print(0)

else:
    a, b = 0, 1
    for i in range(2, N+1):
        a, b = b, a + b
        print ( str(i) + "-й эллемент =", b)
