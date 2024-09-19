import sys
input = sys.stdin.readline

# N = int(input())
# result = 0
# li = [0] + list(map(int, input().split()))
# for i in range(1, N+1):
#     if li[i] < max(li[i:]): result = max(result, max(li[i:]) - li[i])
#     else: continue

# print(result)

N = int(input())
li = list(map(int,input().split()))
max_val = result = 0
for i in range(N-1, -1, -1):
    max_val = max(max_val, li[i])
    result = max(result, max_val - li[i])

print(result)