N = int(input())

dic ={}
li = list(map(str, input().split()))

for i in li:
    if i[-1: -7: -1] == "eseehC":
        dic[i] = 1

if len(dic) >= 4:
    print("yummy")
else:
    print("sad")
