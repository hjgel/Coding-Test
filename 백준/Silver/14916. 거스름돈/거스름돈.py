N = int(input())

dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4]

for i in range(9, N+1):
    dp.append(dp[i-5] + 1)

print(dp[N])