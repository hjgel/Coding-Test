from collections import Counter

li = []
n = int(input())
for _ in range(n):
    a = input()
    li.append(a)

li1 = Counter(li)
max_val = max(li1.values())

best = []
for key, value in li1.items():
    if value == max_val:
        best.append(key)

best = sorted(best)
print(best[0])
