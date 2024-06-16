def dfs(x, y):
    if 0 > x or x >= N or y < 0 or y >= N:
        return False
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            dfs(nx,ny)
        return True
    return False

cnt = 0
graph = []
danzi = []
total = 0

N = int(input())
for _ in range(N): graph.append(list(map(int, input())))
    
for i in range(N):
    for j in range(N):
        if dfs(i,j): 
            danzi.append(cnt)
            total += 1
            cnt = 0

danzi.sort()
print(total)
for d in danzi: print(d)
