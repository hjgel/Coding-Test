for i in range(int(input())):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])