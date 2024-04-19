N= int(input())
li = list(range(1,N+1))
result_li = []

while len(li) > 1:
    result_li.append(li.pop(0))
    li.append(li.pop(0))

result_li.append(li.pop())

print(*result_li)