n = int(input())
mid = n // 2
for i in range(n):
    for j in range(n):
        print('*' if i == mid or j == mid else ' ', end='')
    print()
