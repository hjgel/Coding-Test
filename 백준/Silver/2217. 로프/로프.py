N = int(input())
li =[]

for i in range(N):
    s = int(input())
    li.append(s)
li.sort()

answers = []
for x in li:
    answers.append(x*N)
    N -= 1
print(max(answers))