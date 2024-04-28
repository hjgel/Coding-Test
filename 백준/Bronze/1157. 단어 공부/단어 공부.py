N = input().upper()
li_N = list(set(N))
result = []

for i in li_N:
    result.append(N.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(li_N[result.index(max(result))])
