n = int(input())
total = 0
for i in range(1, n + 1):
    total += -i if i % 2 == 0 else i
print(total)
