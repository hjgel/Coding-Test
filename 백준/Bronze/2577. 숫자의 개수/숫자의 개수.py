A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)
result_set = set(result)

li = [0] * 10

for i in result_set:
    cnt = result.count(i)
    li[int(i)] = cnt

for j in li:
    print(j)