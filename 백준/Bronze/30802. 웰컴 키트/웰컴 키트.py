import math

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
shirt = 0

for i in range(len(size)):
    shirt += math.ceil(size[i]/T)   
    
print(shirt)
print(N//P, N%P)