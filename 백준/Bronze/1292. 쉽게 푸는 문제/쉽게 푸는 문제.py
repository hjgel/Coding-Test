li = []
for i in range(1, 1001):
    for j in range(1, i+1):
        li.append(i)

n, k = map(int, input().split())

total = 0
for i in li[n-1:k]:
    total += i

print(total)