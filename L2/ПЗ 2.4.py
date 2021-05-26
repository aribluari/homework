n = int(input('Введите число: '))
l = list(str(n))                # список из заданных чисел
k = int(len(l))                 # сумма заданных чисел

for i in l:
    k -= 1
    if k != 0:
         print (f'{i}*10^{k}', end = ' + ')
    else:
        print(f'{i[-1]} = {n}', end = '')
