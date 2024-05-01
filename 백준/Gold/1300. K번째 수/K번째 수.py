i = int(input())
j = int(input())

start = 1
end = i * i
B_k = 0 
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for idx in range(1, i + 1):
        cnt += min(mid // idx, i)

    if cnt >= j:
        B_k = mid
        end = mid - 1
    else:
        start = mid + 1

print(B_k)

