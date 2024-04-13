cnt = 0

N, M = map(int, input().split())
a = set()

for i in range(N):
    a.add(input())

for _ in range(M):
    s = input()
    if s in a:
        cnt +=1
        

print(cnt)
