M = int(input())
N = int(input())
num = 1
total = 0
min_val = 0
for i in range(1, 101):
    if i * i >= M and i * i <= N:
        if total == 0:
            min_val = i * i
        total = total + (i * i)

if total:
    print(total)
    print(min_val)
else:
    print(-1)