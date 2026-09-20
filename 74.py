import math
x = float(input())
n = int(input())
total = 0
for i in range(n):
    power = 2 * i + 1
    term = x ** power / math.factorial(power)
    total += term if i % 2 == 0 else -term
print(total)
