a, b, c = map(int, input().split())
print('Valid Triangle' if a + b > c and a + c > b and b + c > a else 'Invalid Triangle')
