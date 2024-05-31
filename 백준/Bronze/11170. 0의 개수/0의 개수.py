for _ in range(int(input())):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        for k in str(i):
            cnt += k.count("0")
    print(cnt)