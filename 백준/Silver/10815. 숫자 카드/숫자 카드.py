def binarySearch(li, target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if li[mid] == target:
            return True
        elif li[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 
    return False 
        

N = int(input())
find_card = list(map(int, input().split()))
F = int(input())
card = list(map(int, input().split()))
find_card.sort()

for i in card:
    if binarySearch(find_card, i, 0, N-1):
        print(1, end= " ")
    else:
        print(0, end= " ")