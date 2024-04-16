N = input()
li = []
for i in range(len(N)):
    li.append(N[i:])

li.sort()
for i in li:
    print(i)