def print_pattern(n, current=1):
    if current > n:
        return
    print(current, end=' ')
    print_pattern(n, current + 1)
    print(current, end=' ')

print_pattern(int(input()))
