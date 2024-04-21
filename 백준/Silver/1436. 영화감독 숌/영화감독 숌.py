jong = 666
N = int(input())
cnt = 0

while True:
    if '666' in str(jong):  
        cnt += 1
    
    if cnt == N:
        break

    jong += 1

print(jong)
