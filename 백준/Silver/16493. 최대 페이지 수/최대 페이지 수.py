K, N = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
page = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= page[i-1][0]:
            dp[i][j] = max(page[i-1][1] + dp[i-1][j-page[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N][K])
