N = int(input())
start_n = N
cnt = 0

while True: 
    a = N // 10
    b = N % 10
    N = (b*10) + (a+b) % 10
    cnt += 1
    if start_n == N:
        break

print(cnt)