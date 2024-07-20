N, K = map(int, input().split())

a, b = 1, 1
for _ in range(4, N+1):
    a, b = b, a+b

A = 1
B = 0
while True:
    tmp = K - a * A
    if tmp < 0:
        break

    if tmp % b == 0:
        B = tmp // b
        break

    A += 1

print(A)
print(B)