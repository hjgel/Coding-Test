A = input()
B = input()

LCS = [[""] * (len(B) +1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]: LCS[i][j] = LCS[i - 1][j - 1] + A[i-1]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
to = LCS[-1][-1]
print(len(to), to)