cnt = 0
for _ in range(int(input())):
    a = input()
    st = ""
    for i in a:
        if i not in st:
            st += i
        elif i in st: 
            if st[-1] == i:
                st += i
            else:
                cnt -= 1
                break
    
    cnt += 1

print(cnt)
