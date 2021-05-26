def low(a):
    return a.lower()
print(low('Hellooo'))

def up(a):
    return a.upper()
print(up('Helloo'))

c = ['a', 'B',  'c', 'D']
f = ['f', 'n', 'B', 'G']

c = list(map(low, c))
print(c)
f = list(map(up, f))
print(f)
