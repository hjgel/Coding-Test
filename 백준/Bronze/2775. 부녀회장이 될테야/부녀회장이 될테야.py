N = int(input())
for _ in range(N):
    k = int(input())
    n = int(input())
    dp = [[1] * (n) for _ in range(k+1)]
    dp.insert(0, [1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    for i in range(1, k+2):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[k][n-1])