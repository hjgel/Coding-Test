for _ in range(int(input())):
    a = list(map(str, input().split()))
    for i in range(len(a)):
        a[i] = a[i][::-1]
    print(*a)