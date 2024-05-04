import sys
input = sys.stdin.readline()

A, P = map(int, input.split())
li = [A]
while True:
    total = 0
    for i in str(li[-1]):
        total += int(i) ** P

    if total in li:
        break
    li.append(total)

print(li.index(total))