N, K = map(int, input().split())
cnt = 0
i = 1
while N >= i:

    if N % i == 0:
        cnt += 1

    if cnt == K:
        break
    i += 1

if i > N: print(0)
else: print(i)