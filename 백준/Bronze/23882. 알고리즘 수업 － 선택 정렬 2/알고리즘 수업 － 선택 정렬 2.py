a, b = map(int, input().split())
arr = list(map(int, input().split()))
game = 0

for i in range(len(arr) - 1, 0, -1):
    idx = arr.index(max(arr[:i + 1])) # 0부터 i까지 중 제일 큰 수를 담음. idx = 인덱스값. 
    if idx != i: # 인덱스가 서로 같지 않으면
        arr[idx], arr[i] = arr[i], arr[idx] # 현재 인덱스랑 제일 큰 인덱스랑 값 변경
        game += 1 # count하나 올려줌
        if game == b: # count가 바꾼 횟수랑 같으면 
            print(*arr) # 리스트 띄우고
            exit() # 종료. 아래는 무시함.
            
print(-1) # 만약 if문이 안 작동하면 횟수를 넘은 것 밖에 없기 때문에 그냥 -1 띄우고 종료.
