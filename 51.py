n = int(input())
original = n
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print('Palindrome' if original == reverse else 'Not Palindrome')
