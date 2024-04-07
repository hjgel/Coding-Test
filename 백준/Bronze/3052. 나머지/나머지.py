li = []

for i in range(10):
    li.append(int(input()))
    li[i] = li[i] % 42

li = list(set(li))
print(len(li))