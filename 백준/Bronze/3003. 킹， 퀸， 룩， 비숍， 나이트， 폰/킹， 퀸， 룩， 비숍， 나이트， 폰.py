li = [1,1,2,2,2,8]
N = list(map(int, input().split()))

for i in range(len(li)):
    print(li[i] - N[i], end=" ")
