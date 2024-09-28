import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = []


def back(start):
    if len(li) == M:
        print(' '.join(map(str, li)))
        return
    for i in range(start, N + 1):
        if i not in li:
            li.append(i)
            back(i+1)
            li.pop()

back(1)