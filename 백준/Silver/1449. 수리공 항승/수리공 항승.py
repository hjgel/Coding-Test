N, L = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

start = li[0]
cnt = 1

for i in li[1:]:
    if (i+0.5) - (start-0.5) <= L:
        continue
    else: 
        start = i
        cnt += 1
print(cnt)