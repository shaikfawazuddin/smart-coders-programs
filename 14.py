n, k = map(int, input().split())
print('Set' if n & (1 << k) else 'Not set')
