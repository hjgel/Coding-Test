from collections import defaultdict, Counter
N = int(input())
n = list(map(int, input().split()))

M = int(input())
m = list(map(int, input().split()))

nH = Counter(n)

for i in range(len(m)):
    if m[i] in nH:
        m[i] = nH[m[i]]
    else:
        m[i] = 0
    
    print(m[i], end =" ")