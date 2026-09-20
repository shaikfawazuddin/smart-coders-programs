count = 0
total = 0
while True:
    n = float(input())
    if n == -1:
        break
    total += n
    count += 1
if count > 0:
    print('Count:', count)
    print('Average:', total / count)
else:
    print('No numbers entered')
