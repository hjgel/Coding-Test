n = int(input())

ans = False
while True:
    for i in str(n):
        if i == "7" or i == "4":
            ans = True
        else: 
            ans = False
            break
    if ans == True: 
        print(n)
        break
    n -= 1