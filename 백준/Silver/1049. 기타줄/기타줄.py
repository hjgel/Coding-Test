N, M = map(int, input().split())
package = []
eachs = []
price = 0

for i in range(M):
    pack, each = map(int, input().split())
    package.append(pack)
    eachs.append(each)

while N > 0:
    re = min(6, N)
    if min(package) <= min(eachs) * re:
        if 6 >= N:
            price += min(package)
            break
        price += min(package)
        N -= 6
    else: 
        price += min(eachs) * N
        break
   
print(price)