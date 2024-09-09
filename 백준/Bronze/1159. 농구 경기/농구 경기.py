li = [input() for _ in range(int(input()))]

li.sort()

k = li[0][0]
total = 1
re = ""
for i in li[1:]:
    if i[0] == k: total += 1
    else: 
        k = i[0]
        total = 1

    if total == 5: re += k
if re == "": print("PREDAJA")
else: print(re)