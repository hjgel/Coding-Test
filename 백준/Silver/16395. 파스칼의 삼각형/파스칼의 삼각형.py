n, k = map(int, input().split())
dp = [[] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0 or j == 0 or j == i: dp[i].append(1)
        else: dp[i].append(dp[i-1][j-1] + dp[i-1][j])

print(dp[n-1][k-1])