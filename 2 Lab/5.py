# В восточном календаре принят 60-летний цикл, состоящий из 12-летних
# подциклов, обозначаемых названиями цвета: зеленый, красный, желтый, белый
# и черный. В каждом подцикле годы носят названия животных: крысы, коровы,
# тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
# По номеру года определить его название, если 1984 год — начало цикла: «год зеленой крысы».


# зеленый, красный, желтый, белый и черный
#крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи
year = int( input( "Enter year " ) )
sh = ( year - 1984 )
collorTemp = sh % 60

print("YEAR IS", end=" ")
if (collorTemp >= 0) and (collorTemp < 12):
    print("Green", end=" ")
elif (collorTemp >= 12) and (collorTemp < 24):
    print("Red", end=" ")
elif (collorTemp >= 24) and (collorTemp < 36):
    print("Yellow", end=" ")
elif (collorTemp >= 36) and (collorTemp < 48):
    print("White", end=" ")
elif (collorTemp >= 48) and (collorTemp < 60):
    print("Black", end=" ")

if sh % 12 == 11:
    print("pig", end=" ")
elif sh % 12 == 0:
    print("rat", end=" ")
elif sh % 12 == 1:
    print("ox", end=" ")
elif sh % 12 == 2:
    print("tiger", end=" ")
elif sh % 12 == 3:
    print("rabbit", end=" ")
elif sh % 12 == 4:
    print("dragon", end=" ")
elif sh % 12 == 5:
    print("snake", end=" ")
elif sh % 12 == 6:
    print("horse", end=" ")
elif sh % 12 == 7:
    print("GOAT", end=" ")
elif sh % 12 == 8:
    print("monkey", end=" ")
elif sh % 12 == 9:
    print("rooster", end=" ")
elif sh % 12 == 10:
    print("dog", end=" ")
