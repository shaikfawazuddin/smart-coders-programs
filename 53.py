def product_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)

print(product_digits(int(input())))
