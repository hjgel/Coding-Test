import sys
input = sys.stdin.readline
def prime_numbers(n):
    arr = [i for i in range(n+1)] # 인덱싱을 수월하게 하기 위해 0부터 배열 선언
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: # 이미 소수가 아님이 판별된 수는 건너뜀
            continue
        for j in range(i*i, n+1, i): # 자기 자신을 제외한 i의 배수는 모두 0으로 처리함.
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

N = int(input())
li = prime_numbers(N)

left = 0
right = 0
cnt = 0
while right <= len(li):
    total = sum(li[left:right])
    if total == N:
        cnt += 1
        right += 1
    elif total > N:
        left += 1
    elif total < N:
        right += 1
print(cnt)