li = [list(map(int, input().split())) for _ in range(int(input()))]
li = sorted(li, key=lambda x : (x[1], x[0]))

i = 0
last = 0

for start, end in li:
    if last <= start:
        i += 1
        last = end
print(i)
