a, b = map(int, input().split())
x, y = abs(a), abs(b)
while y:
    x, y = y, x % y
gcd = x
print(abs(a * b) // gcd if gcd else 0)
