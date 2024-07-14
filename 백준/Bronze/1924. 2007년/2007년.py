date = 0
cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yo = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
for i in range(x-1):
    date += cal[i]
date = (date + y) % 7

print(yo[date])
