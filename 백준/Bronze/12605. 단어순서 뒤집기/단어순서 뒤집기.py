for i in range(int(input())):
    li = list(map(str, input().split()))
    if len(li) > 1:
        li.reverse()
    st = f"Case #{i + 1}:"
    print(st, *li)