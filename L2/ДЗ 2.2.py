a = int(input('Введите число: '))
b = True if a > 50 else False
c = True if not a % 2 else False
print('Данное число больше 50: '+ str(b))
print('Данное число делится на 2: '+ str(c))
