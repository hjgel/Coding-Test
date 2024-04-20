li = []
result = []

for _ in range(int(input())):
    score = list(reversed(list(map(int, input().split()))))
    li.append(score)

li.sort(reverse=True)
i = 0
while len(result) != 3:
    if result.count(li[i][2]) < 2:
        print(li[i][2], li[i][1])
        result.append(li[i][2])
    i += 1