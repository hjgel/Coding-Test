k, n = map(int, input().split())
li = []
for _ in range(k): li.append(int(input()))

start = 1
end = max(li)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in li: cnt += (i // mid)
    if cnt >= n: start = mid + 1
    else: end = mid -1

print(end)