a, b = map(float, input().split())
print('Sum:', a + b)
print('Difference:', a - b)
print('Product:', a * b)
if b != 0:
    print('Quotient:', a / b)
    print('Remainder:', a % b)
else:
    print('Division by zero is not allowed')
