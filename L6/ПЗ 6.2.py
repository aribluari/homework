def up(a):
    return a.upper()

running = True

while running:
    star = int(input('Введите положительное нечетное число: '))
    if star == 0:
        print('Введите число которое будет больше нуля и будет нечетным.')
    elif star < 0:
        print('Это число отрицательно. Попробуйте ещё раз.')
    elif star % 2 == 0:
        print('Это четное число. Попробуйте ещё раз.')
    else:
        running = False

list_star = list(range(1, star + 1))

for i in list_star:
    if i % 2 == 0:
        s = i
    else:
        m = i
        k = (star - m) // 2
        print(' '* k + '*' * m )

list_star.pop(-1)

for i in reversed(list_star):
    if i % 2 == 0:
        s = i
    else:
        m = i
        k = (star - m) // 2
        print(' '* k + '*' * m )

print(up('shine bright like a diamond!'))