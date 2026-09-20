n = int(input())
original = n
digits = len(str(abs(n)))
total = 0
while n > 0:
    total += (n % 10) ** digits
    n //= 10
print('Armstrong' if total == original else 'Not Armstrong')
