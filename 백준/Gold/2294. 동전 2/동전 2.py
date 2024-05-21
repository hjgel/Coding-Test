a, b = map(int, input().split())

dp = [b+1] * (b+1)
dp[0] = 0
li = []
for _ in range(a): li.append(int(input()))

li = sorted(list(set(li)))

for i in li:
    for idx in range(i, b+1):
        if dp[idx] > 0: dp[idx] = min(dp[idx], dp[idx-i] + 1)

if dp[b] == b+1: print(-1)
else: print(dp[b])