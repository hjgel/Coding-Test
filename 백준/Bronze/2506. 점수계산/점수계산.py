N = int(input())
li = list(map(int, input().split()))

cnt = 0
total = 0
for i in range(len(li)):
    if li[i] == 0:
        cnt = 0
    else:
        cnt += 1
        total += cnt
print(total)
