N = int(input())
dizip = str(format(N, "b"))
dizip = dizip[::-1]

print(int('0b'+ dizip, 2))
