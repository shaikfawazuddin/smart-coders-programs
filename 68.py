n = abs(int(input()))
if n == 0:
    print('Largest:', 0)
    print('Smallest:', 0)
else:
    largest, smallest = 0, 9
    while n > 0:
        digit = n % 10
        largest = max(largest, digit)
        smallest = min(smallest, digit)
        n //= 10
    print('Largest:', largest)
    print('Smallest:', smallest)
