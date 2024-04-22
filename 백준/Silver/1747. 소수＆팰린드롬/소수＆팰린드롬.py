N = int(input())

def sosu(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

while True:
    if sosu(N):
        Tr = str(N)
        rev = Tr[-1::-1]
        if Tr == rev:
            print(N)
            break
    N += 1