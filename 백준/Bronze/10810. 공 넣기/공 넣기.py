N, M = map(int, input().split())
li = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        li[idx-1] = k

for i in li:
    print(i, end=" ")