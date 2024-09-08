n = int(input())

li = list(map(int, input().split()))
li.sort()

k = 1
for i in li:
    if k < i: break

    k += i

print(k)