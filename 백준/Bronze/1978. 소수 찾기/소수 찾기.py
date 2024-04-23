N = int(input())
li = list(map(int, input().split()))
cnt = 0
def sosu(k):
    if k < 2:
        return False
    f = 2
    while f * f <= k:
        if k % f == 0:
            return False
        f += 1
    return True

for i in li:
    if sosu(i): cnt += 1

print(cnt)