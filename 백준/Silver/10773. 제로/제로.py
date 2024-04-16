N = int(input())
li = []
price = 0
for i in range(N):
    num = int(input())
    if num:
        li.append(num)
    else:
        li.pop()

for i in li:
    if not li:
        print(0)
    else:
        price += i
print(price)