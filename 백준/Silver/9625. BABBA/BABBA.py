n = int(input())
dp = [[0, 1], [1, 1]]
for i in range(2, n):
    dp.append([dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]])

print(dp[n-1][0], dp[n-1][1])
    
