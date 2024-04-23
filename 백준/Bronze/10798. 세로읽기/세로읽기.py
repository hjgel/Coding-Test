li = []
for _ in range(5):
    li.append(input())
string = ""

for i in range(15):
    for j in range(5):
        if i < len(li[j]):
            string += li[j][i]

print(string)