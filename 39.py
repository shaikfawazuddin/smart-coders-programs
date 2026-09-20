hours = float(input())
rate = float(input())
salary = hours * rate if hours <= 40 else 40 * rate + (hours - 40) * rate * 1.5
print(salary)
