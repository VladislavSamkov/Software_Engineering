value = int(input('Введите число от 0 до 10: '))
if value >= 0 and value <= 3:
    print('Диапазон от 0 до 3')
elif value > 3 and value <= 6:
    print('Диапазон от 4 до 6')
elif value > 6 and value <= 10:
    print('Диапазон от 7 до 10')
else:
    print('Значение за диапазоном 0-10')