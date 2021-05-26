#Банкомат который выдает сумму максимально возможными купюрами
bills = [1000, 500, 200, 100, 50, 20, 10]

while True:
    money = int(input('Введите сумму которую вы хотите снять: '))
    if money % bills[-1] != 0:
      print('Минимальная доступная купюра: ' + str(bills[-1]) + '$\n')
    else:
        break

for i in bills:
    k = money // i
    money -= (i * k)
    print((str(i) + '$ ') * k, end = '')
print('\nХорошего дня!')







