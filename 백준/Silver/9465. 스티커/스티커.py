for _ in range(int(input())):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]
    if N > 1:
        dp[0][1] = li[1][0] + li[0][1]
        dp[1][1] = li[0][0] + li[1][1]

    for j in range(2, N):
        dp[0][j] = max(dp[1][j-2], dp[1][j-1]) + li[0][j]
        dp[1][j] = max(dp[0][j-2], dp[0][j-1]) + li[1][j]
    print(max(dp[0][N-1], dp[1][N-1]))