for _ in range(int(input())):
    N, S = map(str, input().split())
    for i in range(len(S)):
        print(S[i] * int(N), end="")
    print()