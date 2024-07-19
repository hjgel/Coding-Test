N = int(input())
li = [list(map(str, input().split())) for _ in range(N)]

li = sorted(li, key= lambda x : (int(x[3]), int(x[2]), int(x[3])))
print(li[-1][0])
print(li[0][0])