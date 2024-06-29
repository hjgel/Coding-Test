import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int ,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
visited[R] = 1
cnt = 1 

q = deque([R])
while q:
    r = q.popleft()
    graph[r].sort()
    for i in graph[r]:
        if visited[i] == 0:
            q.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]: print(i)
