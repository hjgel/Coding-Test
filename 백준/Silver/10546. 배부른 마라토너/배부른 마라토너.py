from collections import defaultdict, Counter
def solution(participant, completion):
    answer = ''
    sH = Counter(participant)
    for x in completion:
        sH[x] -= 1
    for key in sH:
        if sH[key] == 1:
            return key
    return answer


n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())
print(solution(a, b))