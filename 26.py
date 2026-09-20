n = int(input())
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days[n - 1] if 1 <= n <= 7 else 'Invalid')
