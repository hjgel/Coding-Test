for i in range(int(input())):
    print("Class", (i+1))
    li = list(map(int, input().split()))
    li.pop(0)
    li.sort(reverse=True)
    gap_val = li[0] - li[1]
    for j in range(2, len(li)):
        gap_val = max(gap_val, li[j - 1] - li[j])

    print(f"Max {max(li)}, Min {min(li)}, Largest gap {gap_val}")