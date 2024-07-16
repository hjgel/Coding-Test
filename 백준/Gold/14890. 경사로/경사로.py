import sys
input = sys.stdin.readline

def check(l, v):
    cnt = 1  # 연속된 동일 숫자의 개수 카운트
    for i in range(1, len(l)):
        if l[i-1] == l[i]: cnt += 1
        elif l[i-1] + 1 == l[i] and cnt >= L and v[i-L:i] == [0] * L:
            cnt = 1          
            v[i-L:i] = [1] * L
        elif l[i-1] > l[i]: cnt = 1
        else: return False
    return True

N, L = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for _ in range(2):    
    for l in li:
        v = [0] * (len(l)) 
        if check(l, v) and check(l[::-1], v[::-1]): answer += 1
    li = list(map(list, zip(*li))) # 2차원 리스트 90도 회전!
print(answer)
