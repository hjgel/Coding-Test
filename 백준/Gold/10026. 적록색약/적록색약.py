import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited= [[False] * N for _ in range(N)]

cnt1, cnt2 = 0, 0 

dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == False:
                if color == graph[nx][ny]:
                    dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if visited[i][j] == False: 
            dfs(i,j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == "R": graph[i][j] = "G"

visited= [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            cnt2 += 1
print(cnt1, cnt2)
