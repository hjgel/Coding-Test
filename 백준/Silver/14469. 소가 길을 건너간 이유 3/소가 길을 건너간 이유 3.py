N = int(input())
check = {}
arr = []

for i in range(N):
    arrive, time = map(int, input().split())
    check[arrive] = time
    arr.append(arrive)

arr.sort()
timer = 0
timer += arr[0] + check[arr[0]]

for i in arr[1:]:
    if timer <= i:
        timer = i + check[i]
    else:
        timer += check[i]

print(timer)
