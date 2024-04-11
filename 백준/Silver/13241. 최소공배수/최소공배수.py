def gcd(a, b):
    
    if(b == 0):
        return a
    return gcd(b, a%b)

def shortGcd(a,b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(shortGcd(a,b))