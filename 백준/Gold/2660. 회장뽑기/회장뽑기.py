import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
dp = [[INF] * (n+1) for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1: break
    dp[a][b] = 1
    dp[b][a] = 1
    
for i in range(1, n+1):
    dp[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] == 1 or dp[i][j] == 0: continue
            else: dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

li = []
for i in range(1, n+1): li.append(max(dp[i][1:]))
m = min(li)
print(m, li.count(m))
for a, b in enumerate(li):
    if b == m: print(a+1, end=" ")