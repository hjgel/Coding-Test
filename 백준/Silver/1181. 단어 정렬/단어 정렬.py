a = int(input())
li = []

for _ in range(0, a):
    b = input()
    li.append(b)

li = list(set(li)) # set = 중복값을 없애주고 오름차순으로 정렬해줌.

li.sort()
li.sort(key=lambda x : len(x))

for i in li:
    print(i)

