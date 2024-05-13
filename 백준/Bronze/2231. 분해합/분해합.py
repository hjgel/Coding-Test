N = int(input())

def sliceNum(num):
    li = [num]
    while num>0:
        temp=num%10
        li.append(temp)
        num//=10
    return li


for i in range(1, N):
    li = sliceNum(i)
    if sum(li) == N:
        print(i)
        exit()

print(0)