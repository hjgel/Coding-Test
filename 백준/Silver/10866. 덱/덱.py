import sys
from collections import deque

queue = deque()
for i in range(int(input())):
    info = sys.stdin.readline().split()

    if info[0] == "push_front": queue.appendleft(info[1])
    if info[0] == "push_back": queue.append(info[1])
    elif info[0] == "front":
        if queue: print(queue[0])
        else: print(-1)
    elif info[0] == "back": 
        if queue: print(queue[len(queue)-1])
        else: print(-1)
    elif info[0] == "size": print(len(queue))
    elif info[0] == "empty": 
        if queue: print(0)
        else: print(1)
    elif info[0] == "pop_front": 
        if queue: print(queue.popleft())
        else: print(-1)
    elif info[0] == "pop_back":
        if queue: print(queue.pop())
        else: print(-1)