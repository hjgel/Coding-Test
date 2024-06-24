import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split()) # 입력을 받는다.
# N = 접시 개수, D = 초밥 가지수, K = 연속해서 먹는 접시수, C는 쿠폰번호

pan = [int(input()) for _ in range(N)]

eat_sushi = 1 # 쿠폰번호에 있는 초밥은 먹었다는 가정을 둠. 
check = [0] * (D+1) # 초밥의 가지수만큼 만든다! 
check[C] = 1

for i in range(K): # 0부터 K번이 되기 전까지 돌려 
    sushi = pan[i % N] # 스시 값 주기. 0 % 7 = 0임을 이용

    if not check[sushi]: # 스시번 초밥이 check되어있지 않으면 먹는다. 
        eat_sushi += 1 # 냠냠
    check[sushi] += 1 # 그리고 체크해줌

max_sushi = eat_sushi # 저걸 K번동안 반복했을 때 먹은 최대 개수

for i in range(N): # 0부터 N이 되기 전까지 돌린다. 
    start = pan[i % N] # start를 0으로 두고
    end = pan[(i + K) % N] # end를 i + K % N 만큼 둔다. (0 + 4) % 7.. = pan[4] = 2
    
    check[start] -= 1 # start번 초밥을 -1 없애고 
    if check[start] == 0: eat_sushi -= 1 # 그 값이 0이었을 경우 먹은 스시 -1 

    if check[end] == 0: eat_sushi += 1 # end번 초밥이 0이면 스시 + 1
    check[end] += 1  # end번을 한칸 올림. 

    max_sushi = max(max_sushi, eat_sushi)
print(max_sushi)