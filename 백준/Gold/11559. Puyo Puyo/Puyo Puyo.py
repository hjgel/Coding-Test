import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(12)]

def down(): 
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graph[j][i] != '.' and graph[k][i] == '.':
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):   
    q = deque()
    q.append([i,j])
    temp.append([i,j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                q.append([nx,ny])
                temp.append([nx,ny])
                visited[nx][ny] = 1

def delete(t):
    for i, j in t:
        graph[i][j] = '.'

total = 0
while True:
    cnt = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                bfs(i,j)
                if len(temp) >= 4:
                    cnt = 1
                    delete(temp)
    if cnt == 0:
        break
    down()
    total += 1

print(total)



