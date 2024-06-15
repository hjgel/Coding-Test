import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M ) and (0 <= ny < N) and stack[ny][nx] == 1:
            stack[ny][nx] = -1
            dfs(nx, ny)



for _ in range(int(input())):
    M, N, K = map(int, input().split())
    stack = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        stack[Y][X] = 1
    
    count = 0
    for i in range(M):
        for j in range(N):
            if stack[j][i] == 1:
                dfs(i,j)
                count += 1
    print(count)