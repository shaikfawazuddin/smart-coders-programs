rows, cols = map(int, input().split())
for i in range(rows):
    for j in range(cols):
        print('*' if i in (0, rows - 1) or j in (0, cols - 1) else ' ', end='')
    print()
