n = int(input())
for i in range(n):
    for j in range(n):
        print('*' if j == i or j == n - i - 1 else ' ', end='')
    print()
