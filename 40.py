balance = float(input())
amount = float(input())
if amount <= 0: print('Invalid amount')
elif amount > balance: print('Insufficient balance')
elif balance - amount < 500: print('Minimum balance rule violated')
else:
    print('Withdrawal successful')
    print('Remaining balance:', balance - amount)
