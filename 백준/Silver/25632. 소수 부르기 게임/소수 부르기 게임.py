a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())


def prime_numbers(a, b):
    arr = [i for i in range(b+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(b**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, b+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[a:] if arr[i]]

yt = (prime_numbers(a1, b1))
yj = (prime_numbers(a2, b2))

cnt = 0

for i in yt: 
    if i in yj: cnt += 1


if len(yt) > len(yj): print("yt")
elif len(yt) == len(yj): 
    if cnt % 2 == 1: print("yt")
    else: print("yj")
else: print("yj")