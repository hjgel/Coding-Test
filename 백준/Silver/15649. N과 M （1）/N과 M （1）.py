import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []
check = [False] * (N+1)

def back(num):
    if num == M:
        print(' '.join(map(str, li)))
        return
    for i in range(1, N + 1):
        if check[i] == False:
            check[i] = True
            li.append(i)
            back(num+1)
            check[i] = False
            li.pop()
back(0)