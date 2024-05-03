N = int(input())
j = 1
for i in range(N - 1, -1, -1):
    print((" " * i) + ("*" * j))
    j += 2
j -= 2
for i in range(1, N):
    j -= 2
    print((" " * i) + ("*" * j))
    
    
