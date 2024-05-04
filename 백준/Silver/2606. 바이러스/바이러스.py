from collections import deque

N = int(input()) # 컴퓨터 번호(N번까지)
M = int(input()) # 연결 개수

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)

def bfs(v):
    cnt = 0
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in range(1, N + 1):
            if not visited[i] and graph[v][i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

print(bfs(1))