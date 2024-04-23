N = input()
li = [0] * 10

for i in range(len(N)):
    i = int(N[i])
    if i == 6 or i == 9:
        if li[6] <= li[9]:
            li[6] += 1
        else:
            li[9] += 1
    else:
        li[i] += 1

print(max(li))
