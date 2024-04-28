li = []
for _ in range(int(input())):
    age, name = input().split()
    li.append([int(age), name])

for i in sorted(li, key = lambda x : x[0]):
    print(i[0], i[1])