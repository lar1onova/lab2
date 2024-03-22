year = int(input('введите номер года'))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 !=0:
        print('год', year, 'невисокосный')
    else:
        print ('год', year, 'високосный')
else:
    print ('год', year, 'невисокосный')
