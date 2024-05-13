li = []
num = 10000

for i in range(1, num + 1):
    re = i
    while  i > 0:
        re += i % 10
        i //= 10
    li.append(re)

for i in range(1, 10001):
    if i not in li:
        print(i)