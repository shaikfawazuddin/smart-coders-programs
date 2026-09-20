a, b, c = map(int, input().split())
if a == b == c: print('Equilateral')
elif a == b or b == c or a == c: print('Isosceles')
else: print('Scalene')
