import sys

stack = []
for i in range(int(input())):
    info = sys.stdin.readline().split()
    
    if info[0] == "push": stack.append(info[1])
    elif info[0] == "top": 
        if stack: print(stack[len(stack)-1])
        else: print(-1)
    elif info[0] == "size": print(len(stack))
    elif info[0] == "empty": 
        if stack: print(0)
        else: print(1)
    elif info[0] == "pop": 
        if stack: print(stack.pop())
        else: print(-1)
    