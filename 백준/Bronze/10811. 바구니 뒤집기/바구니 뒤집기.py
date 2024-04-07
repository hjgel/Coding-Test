N, M = map(int, input().split())
li = list(range(1, N+1))
temp = 0

for x in range(M):
  i,j = map(int, input().split())
  temp = li[i-1:j]
  temp.reverse()
  li[i-1:j] = temp

for x in range(N):
    print(li[x],end=" ")