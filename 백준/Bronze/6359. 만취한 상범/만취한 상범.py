for _ in range(int(input())):
    n = int(input())
    li = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(2, n+1):
            if j % i == 0:
                if li[j] == 1:
                    li[j] = 0
                else:
                    li[j] = 1
    print(li.count(1) - 1)
    
        
