n = int(input())
for i in range(n):
    value = 1
    print(' ' * (n - i), end='')
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()
