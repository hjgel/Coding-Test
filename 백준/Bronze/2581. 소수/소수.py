N = int(input())
M = int(input())
li = []

for i in range(N, M+1):
    j = 2
    pan = True
    if i > 1:
        while j * j <= i:
            if i % j == 0:
                pan = False
                break
            j += 1 
    else: pan = False
    if pan: li.append(i)
if len(li):
    print(sum(li))
    print(min(li))
else:
    print(-1)