choice = input().upper()
temp = float(input())
if choice == 'C':
    print(temp * 9 / 5 + 32)
elif choice == 'F':
    print((temp - 32) * 5 / 9)
else:
    print('Invalid choice')
