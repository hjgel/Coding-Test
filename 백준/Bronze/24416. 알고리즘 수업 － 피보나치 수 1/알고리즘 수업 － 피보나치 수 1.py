N = int(input())

cnt1, cnt2 = 0, 0
def fib(n):
    a, b = 1, 1
    for i in range(3, n+1): 
        a, b = b, a+b
    return b

def fibonacci(n):
    return n-2

print(fib(N), fibonacci(N))