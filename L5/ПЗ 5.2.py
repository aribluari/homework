def simple_num(n):
    k = 0
    for j in range(2, n):
        if n % j == 0:
            k = k + 1
    if k == 0:
        return n ** 2
    else:
        k = 0
        return 'No'
b = [4, 5, 7, 12, 13, 14, 33, 55, 57, 2]
b = list(map(simple_num, b))
print(b)


