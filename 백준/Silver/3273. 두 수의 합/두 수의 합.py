import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
target = int(input())
li.sort()

cnt = 0
left = 0
right = len(li) - 1
while left < right:
    if li[left] + li[right] == target:
        cnt += 1
        left += 1
        right -= 1
    elif li[left] + li[right] > target:
        right -= 1
    elif li[left] + li[right] < target:
        left += 1
print(cnt)