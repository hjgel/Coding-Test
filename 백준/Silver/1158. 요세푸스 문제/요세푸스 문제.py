N, K = map(int, input().split())
yoshi = list(range(1, N+1))
result = []
k = 0
f = N

for _ in range(f):
    k = (k + K - 1) % N
    result.append(str(yoshi.pop(k)))
    N -= 1



print("<",", ".join(result)[:],">", sep='')
    

