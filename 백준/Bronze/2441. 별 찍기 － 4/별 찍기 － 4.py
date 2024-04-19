N = int(input())

for i in range(N, 0, -1):
    for j in range(0, N-i):
        print(" ", end="")
    print("*" * i)