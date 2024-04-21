li = []
for _ in range(int(input())):
    N = list(map(int, input().split()))
    li.append(N)

for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end= " ")