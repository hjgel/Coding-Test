N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]

memo = [0] * (N + 1) # 메모이제이션

for i in range(N-1, -1, -1):
    if li[i][0] + i > N:
        memo[i] = memo[i+1]
    else:
        memo[i] = max(memo[i + 1], memo[i + li[i][0]] + li[i][1])
print(memo[0])