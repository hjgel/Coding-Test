pipe = input()
stack = []
total = 0

for i in range(len(pipe)):
    if pipe[i] == "(": stack.append(pipe[i])
    else: 
        if pipe[i-1] == "(": 
            stack.pop()
            total += len(stack)
        else:
            stack.pop() 
            total += 1
        
print(total)