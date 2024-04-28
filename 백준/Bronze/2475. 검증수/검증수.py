N = list(map(int, input().split()))
total = 0
for i in range(len(N)):
    if N[i] != 0:
        N[i] **= 2
    total += N[i]

print(total%10)