li = []
for _ in range(9):
    li.append(int(input()))

max_Val = max(li)
index_Val = li.index(max_Val) + 1

print(max_Val)
print(index_Val)