
for _ in range(int(input())):
    li = list(map(int, input().split()))
    li.sort()
    li.remove(min(li))
    li.remove(max(li))
    if max(li) - min(li) >= 4: print("KIN")
    else: print(sum(li))