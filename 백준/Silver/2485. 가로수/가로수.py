def gcd(a, b):
    
    if(b == 0):
        return a
    return gcd(b, a%b)

N = int(input())
one_S = int(input()) # 첫 번째 가로등
li = [] 

for i in range(N-1):
    S = int(input()) # 2~N번째 가로등
    li.append(S-one_S)
    one_S = S

g = li[0]
for j in range(1, len(li)):
    g = gcd(g, li[j])

re = 0
for k in li:
    re += k // g - 1
print(re)