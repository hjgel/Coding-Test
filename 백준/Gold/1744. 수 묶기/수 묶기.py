import sys
input = sys.stdin.readline
n = int(input())

up = []
down = []

total = 0
for _ in range(n):
    su = int(input())
    if su == 1: total += 1
    elif su > 1: up.append(su)
    elif su <= 0: down.append(su)

up.sort(reverse=True)
down.sort()

for i in range(0, len(up), 2):
    if i+1 >= len(up): total += up[i]
    else: total += up[i] * up[i+1]

for i in range(0, len(down), 2):
    if i+1 >= len(down): total += down[i]
    else: total += down[i] * down[i+1]

print(total)