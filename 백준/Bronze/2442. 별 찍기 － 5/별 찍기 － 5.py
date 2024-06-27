N = int(input())
j = 1
for i in range(N):
    print((" " * (N - (i+1))) + ("*" * (i+j)))
    j += 1