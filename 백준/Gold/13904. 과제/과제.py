N= int(input())
point = []
result = 0

dw = [list(map(int, input().split())) for _ in range(N)] # 과제기한, 점수 입력
dw.sort()

for day in range(N, 0, -1):
    while dw and dw[-1][0] >= day: # dw의 값이 있고, dw 정렬한 마지막에 day가 day보다 크거나 같으면
        point.append(dw.pop()[1]) # 맨 마지막 인덱스 [1]번만 pop
    
    if point: # point에 값이 있으면 
        point.sort() # point를 sort! 
        result += point.pop() # result에 point 리스트에서 가장 큰 값 넣어줌. 

print(result)
