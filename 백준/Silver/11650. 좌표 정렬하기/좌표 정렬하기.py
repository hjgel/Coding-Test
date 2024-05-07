N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

li.sort()
for i,j in li:
    print(i, j)