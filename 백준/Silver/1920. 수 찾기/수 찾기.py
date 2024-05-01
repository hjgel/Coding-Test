def binarySort(target):
    global li
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2

        if target == li[mid]:
            return 1
        
        if target < li[mid]:
            right = mid - 1
        else : 
            left = mid + 1
    return 0

N = int(input())
li = list(map(int, input().split()))
li.sort()
S = int(input())
fi_li = list(map(int, input().split()))

for i in fi_li:
    print(binarySort(i))