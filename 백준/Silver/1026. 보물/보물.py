n= int(input())
total = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = sorted(a)
b1 = sorted(b, reverse=True)
for i in range(0, n):
    result = a1[i] * b1[i]
    total += result
print(total)