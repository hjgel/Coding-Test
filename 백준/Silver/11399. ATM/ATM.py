C = int(input())
N = [0] + list(map(int, input().split()))

N.sort()

cnt = 0
result = 0
for i in range(1, C+1):
    cnt += N[i]
    result += cnt

print(result)