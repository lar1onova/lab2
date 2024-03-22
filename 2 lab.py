def cif(x):
    for i in '1234567890':
        if i in x:
            return True


par = input('введите пароль')
if len(par) < 5:
    print('слишком короткий пароль')
elif not(cif(par)):
    print('используйте цифры')
else:
    print('пароль принят')


