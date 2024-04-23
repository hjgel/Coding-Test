
while True:
    N = list(map(int, input().split()))
    if sum(N) == 0:
        break
    max_N = max(N)
    N.remove(max_N)
    if max_N ** 2 == N[0] **2 + N[1] **2:
        print("right")
    else:
        print("wrong")