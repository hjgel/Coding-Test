li = []
st = []
result = False
cnt = 1
for _ in range(int(input())):
    num = int(input())

    while cnt <= num:
        li.append(cnt)
        st.append("+")
        cnt += 1

    if num == li[-1]:
        li.pop()
        st.append("-")
    else:
        result = True
    
if result:
    print("NO")
else:
    for i in st:
        print(i)

