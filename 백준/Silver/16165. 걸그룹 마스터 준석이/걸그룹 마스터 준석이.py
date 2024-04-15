N, M = map(int, input().split())
group = {} # 아이돌 group
idol = {} # 아이돌 소속

# 아이돌 그룹 세팅
for _ in range(N):
    groupName = input() # 팀 이름 받고
    group[groupName] = [] # 아이돌 그룹 초기화
    for _ in range(int(input())): # input()명 만큼 
        idolName = input() # 이름 받아서 
        group[groupName].append(idolName) #리스트로 append()
        idol[idolName] = groupName # idol 소속을 밝힐 딕셔너리도 생성. 
    group[groupName] = sorted(group[groupName]) # 그룹 멤버 이름 정렬


for _ in range(M):
    keyword = input()
    # 1 일때 소속 그룹 출력 나머지는 그룹 맴버 출력
    if int(input()): # 1이면 
        print(idol[keyword]) # idol[team 이름 출력]
    else: # 1이 아니면 
        print('\n'.join(group[keyword])) # 줄바꿈해주면서 group 전원 나열. 