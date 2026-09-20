hour, minute = map(int, input().split())
hour %= 12
angle = abs(hour * 30 + minute * 0.5 - minute * 6)
print(min(angle, 360 - angle))
