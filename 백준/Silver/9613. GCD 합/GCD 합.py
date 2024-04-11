def gcd(a, b):
    
    if(b == 0):
        return a
    return gcd(b, a%b)

N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    val = a[0]
    cnt = 0
    for i in range(1, val+1):
        for j in range(i+1, val+1):
            cnt += gcd(a[i], a[j])
    print(cnt)