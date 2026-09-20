import math
a, b, c = map(float, input().split())
d = b * b - 4 * a * c
if d > 0: print((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
elif d == 0: print(-b / (2 * a))
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print(f'{real}+{imaginary}i')
    print(f'{real}-{imaginary}i')
