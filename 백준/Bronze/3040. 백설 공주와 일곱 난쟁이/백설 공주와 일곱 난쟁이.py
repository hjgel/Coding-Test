import sys
input = sys.stdin.readline
li = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        if sum(li) - li[i] - li[j] == 100: 
            li.pop(i)
            li.pop(j-1)
            for r in li: print(r)
            exit()
