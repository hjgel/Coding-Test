N, T = map(int, input().split())
dp = [[0] * (T+1) for _ in range(N+1)]
time = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, T+1):
        if j >= time[i-1][0]:
            dp[i][j] = max(time[i-1][1] + dp[i-1][j-time[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N][T])