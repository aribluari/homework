#Банкомат выдает суммe мелкими, но не больше 10 штук каждой мелкой купюры
big_bills = [1000, 500, 200, 100]
lil_bills = [50, 20, 10]
while True:
    money = int(input('Введите сумму которую вы хотите снять: '))
    if money % lil_bills[-1] != 0:
      print('Минимальная доступная купюра: ' + str(lil_bills[-1]) + '$\n')
    else:
        break

if money > 800:
    money_for_lb = (money % big_bills[0])
    if money_for_lb > 800:
        money_for_lb -= 200
    money_for_b = money - money_for_lb
elif money <= 800:
    money_for_lb = money
    money_for_b = 0

for b in big_bills:
    k = money_for_b // b
    money_for_b -= (b * k)
    print((str(b) + '$ ') * k, end='')

for l in lil_bills:
    q_lb = 10
    s = l * q_lb
    k = money_for_lb // l
    if money_for_lb <= s:
        money -= (l * k)
        print((str(l) + '$ ') * k, end='')
    elif money_for_lb >= s:
        money_for_lb -= s
        print((str(l) + '$ ') * q_lb, end='')

print('\nХорошего дня!')
