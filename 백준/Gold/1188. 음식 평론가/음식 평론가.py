def gcd(a, b):
    
    if(b == 0):
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())

if a % b == 0:
    print(0)
else: 
    print(b - gcd(a,b))
