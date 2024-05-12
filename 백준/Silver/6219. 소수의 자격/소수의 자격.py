A, B, D = map(int, input().split())
cnt = 0
array = [0]*(B+1)
for i in range(2, int(B**0.5)+1):
    if array[i] == 0:
        for j in range(i*i,B+1,i):
            array[j] = 1
x = [i for i in range(A,B+1) if array[i] == 0]

for i in x:
    if str(D) in str(i):
        cnt += 1
print(cnt)