dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
N = input()
result = 0
for i in range(len(N)):
    for j in dial:
        if N[i] in j:
            result += dial.index(j) + 3
print(result)