N = int(input())
num = int(input())

result=[]
def sliceNum(num):
    while num>0:
        temp=num%10
        result.insert(0,temp)
        num//=10
    return result

sliceNum(num)
print(sum(result))