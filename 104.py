n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print('*' * (2 * n - 1))
    else:
        print('*' + ' ' * (2 * i - 3) + '*')
for i in range(n - 1, 0, -1):
    if i == 1:
        print('*' * (2 * n - 1))
    else:
        print('*' + ' ' * (2 * i - 3) + '*')
