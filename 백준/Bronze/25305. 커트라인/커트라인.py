N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
print(li[M-1])