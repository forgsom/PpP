#Дано вещественное число – цена 1 кг конфет. Вывести стоимость 0.1, 0.2, …, 1кг конфет.


price = int( input("Enter price ") )

for i in range(1, 11):
    if i == 10:
        print( "1 кг =", str(price) + "р.")
    else:
        print( "0." + str(i), "кг =", str(price / 10 * i) + "р." )
