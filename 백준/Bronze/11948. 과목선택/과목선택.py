li1 = []
li2 = []

for i in range(6):
    if i <= 3: li1.append(int(input()))
    else: li2.append(int(input()))

li1.sort(reverse=True)
print(sum(li1[0:3]) + max(li2))