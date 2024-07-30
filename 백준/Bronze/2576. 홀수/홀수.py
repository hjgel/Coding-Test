total = 0
choi = 100
for i in range(7):
    a = int(input())
    if a % 2 == 1: 
        total += a
        choi = min(choi, a)

if total == 0: print(-1)
else:
    print(total)
    print(choi)
    
