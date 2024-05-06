def solution(x, y, d, board):
    dx = [-1 ,0, 1, 0]
    dy = [0, 1, 0, -1]
    board[x][y] = 2
    answer = 1
    while True:
        flag = False
        for i in range(4):
            d = (d + 3) % 4 # 반시계 방향 회전
            nx = x + dx[d]
            ny = y + dy[d]
            if board[nx][ny] == 0:
                x = nx
                y = ny
                board[x][y] = 2
                flag = True
                answer += 1
                break
        if flag == False:
            if board[x - dx[d]][y - dy[d]] == 1:
                return answer
            else:
                x -= dx[d]
                y -= dy[d]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(r, c, d, arr))