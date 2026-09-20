marks = float(input())
attendance = float(input())
income = float(input())
print('Eligible' if marks >= 75 and attendance >= 75 and income <= 250000 else 'Not Eligible')
