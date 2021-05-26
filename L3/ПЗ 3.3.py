import sys

filename = "ПЗ 3.2.py"
f = open(filename, 'r')

for line in f:
    print(line[::-1])
f.close()