fizz = int(input('Введите число №1: '))
buzz = int(input('Введите число №2: '))
end = int(input('Введите число №3: '))
t = end + 1
for i in range(1, t):
    if not i % fizz:
        print('F')
    elif not i % buzz:
        print('B')
    elif not i % fizz and not i % buzz:
        print('FB')
    else:
        print(i)