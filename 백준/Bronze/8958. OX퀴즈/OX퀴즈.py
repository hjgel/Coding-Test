for i in range(int(input())):
    st = input()
    cnt = 1
    total = 0
    for j in st:
        if j == "O":
            total += cnt
            cnt += 1
        else:
            cnt = 1
    print(total)