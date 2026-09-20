n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*' if j == 1 or j == i or i == n else ' ', end='')
    print()
