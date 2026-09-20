a, b = map(int, input().split())
print(a if a > b else b if b > a else 'Equal')
