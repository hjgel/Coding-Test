N = int(input())
li = []
cnt = 1
for i in range(N):
    k = int(input())
    li.append(k)

last_stick = li[len(li) - 1]

for i in reversed(li):
    if i > last_stick:
        last_stick = i
        cnt += 1
print(cnt)