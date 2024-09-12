N = int(input())

vic = [-1] * 1001

vic[1] = 1
vic[2] = 0
vic[3] = 1
for i in range(4, N+1):
    if vic[i - 1] == 1 or vic[i - 3] == 1: vic[i] = 0
    else: vic[i] = 1

if vic[N] == 1: print("CY")
else: print("SK")