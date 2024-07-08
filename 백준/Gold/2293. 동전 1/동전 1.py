import sys
input = sys.stdin.readline
n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1

li = [int(input()) for _ in range(n)]
li = sorted(list(set(li)))

for i in li:
    for idx in range(i, k+1):
        dp[idx] += dp[idx - i]

print(dp[k])