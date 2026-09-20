n = int(input())
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end=' ')
    print()
