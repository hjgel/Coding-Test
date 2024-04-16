N = int(input())
milk_li = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if milk_li[i] == cnt % 3: cnt +=1
        
print(cnt)