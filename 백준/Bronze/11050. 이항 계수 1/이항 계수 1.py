def Factorial(number) -> int:
    result = 1
    for i in range(2, number + 1):
        result = result * i
    return result

def nCr(n, r) -> int: # 조합 
    return int(Factorial(n) / (Factorial(n-r) * Factorial(r)))

n, r = map(int, input().split())
print(nCr(n,r))