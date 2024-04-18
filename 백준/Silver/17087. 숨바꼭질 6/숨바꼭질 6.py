def gcd(a, b):
    
    if(b == 0):
        return a
    return gcd(b, a%b)


N, S = map(int, input().split())
D = list(map(int, input().split()))

li = []
    
for i in range(len(D)):
    if D[i] < S:
        D[i] = S - D[i]
    elif D[i] > S:
        D[i] -= S
    else :
        del D[i]

for i in range(len(D)):
    li.append(gcd(D[i], D[i-1]))

print(min(li))