num = int(input('введите номер места'))
if num in range(1,56):
    if num % 2 == 0:
        type1 = 'нижнее место'
    else:
        type1 = 'верхнее место'
    if num > 36:
        type2 = 'сбоку'
    else:
        type2 = 'не сбоку'
    print(type1,type2)
else:
    print('ошибка ввода места')
