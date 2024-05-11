N = int(input())
cnt = 0
result = 0
for i in range(2, 10000000):
    if cnt == N:
        break
    else:
        j = 2
        pan = True
        while j * j <= i:
            if i % j == 0:
                pan = False
                break
            j += 1 
        if pan: 
            cnt += 1
            result = i    
print(result)