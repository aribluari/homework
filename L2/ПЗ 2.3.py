number = int(input("Введите целое число,для того чтобы узнать его делители: "))
for i in range(number -1, 0, -1):
    if (number % i == 0):
        print(i)