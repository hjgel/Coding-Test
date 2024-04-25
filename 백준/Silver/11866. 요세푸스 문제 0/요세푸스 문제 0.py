n, k = map(int, input().split())
li = list(range(1, n + 1)) #둥글게 모여앉은 사람들
i = 0
result = []

for idx in range(n): #n번만 반복하면 되니까
	i = (i + k - 1) % len(li)
	result.append(li.pop(i))

print('<' + str(result)[1:-1] + '>')
