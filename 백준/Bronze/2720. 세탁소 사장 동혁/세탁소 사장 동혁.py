N = int(input())
price = []

for i in range(N):
    balance = int(input())
    print(balance // 25, end= " ")
    balance %= 25
    print(balance // 10, end= " ")
    balance %= 10
    print(balance // 5, end= " ")
    balance %= 5
    print(balance // 1)