import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

while True:
    a, b = map (int, input().split())

    if a == b == 0: break
    board = [list(input().rstrip()) for _ in range(a)]

    for x in range(a):
        for y in range(b):
            if board[x][y] == "*": continue

            cnt = 0
            for d0, d1 in d:
                dx, dy = d0 + x, d1 + y
                if dx >= a or dx < 0 or dy >= b or dy < 0: continue

                if board[dx][dy] == "*": cnt += 1
            
            board[x][y] = str(cnt)

    for re in board: print(''.join(re))
    
