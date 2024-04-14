N = int(input())
dic = {}
cnt = 0
for _ in range(N):
    i = input()
    if i == "ENTER":
        dic = {}
        continue
    elif i in dic.keys():
        continue
    else:
        dic[i] = 1
        cnt +=1

print(cnt)