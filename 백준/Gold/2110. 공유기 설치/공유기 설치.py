n, c = map(int, input().split())
li = []

for _ in range(n):
    li.append(int(input()))
li.sort()

start = 1
end = li[-1] - li[0]
total = 0

while start <= end:
    mid = (start + end) // 2
    now = li[0]

    cnt = 1
    for i in range(1, len(li)):
        if li[i] >= now + mid:
            cnt += 1
            now = li[i]
    if cnt >= c:
        start = mid + 1
        total = mid
    else: end = mid - 1

print(total)