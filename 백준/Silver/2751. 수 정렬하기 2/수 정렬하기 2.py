import sys
input=sys.stdin.readline


li = []
for i in range(int(input())):
    li.append(int(input()))


for i in sorted(li):
    print(i)