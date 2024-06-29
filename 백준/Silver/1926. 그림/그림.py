import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = []
    queue.append([x, y])
    maxV = 1
    while queue:
        mx, my = queue.pop()
        for k in range(4):
            nx = mx + dx[k]
            ny = my + dy[k]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append([nx,ny])
                    maxV += 1
    return maxV


cnt = 0
maxVal = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            maxVal = max(maxVal, bfs(i, j))
            cnt += 1

print(cnt)
print(maxVal)
