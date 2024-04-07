li = []
find_li = list(range(1, 31))
for i in range(28):
    li.append(int(input()))
    if li[i] in find_li:
        find_li.remove(li[i])

for j in find_li:
    print(j)
