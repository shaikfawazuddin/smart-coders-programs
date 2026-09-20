a, b = map(int, input().split())
a ^= b
b ^= a
a ^= b
print(a, b)
