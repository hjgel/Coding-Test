N = int(input())
cnt = 1
i = 1
while i < N:

    i += 6 * cnt  # 6 * 1.. 6 * 2... 6*3..
    cnt += 1

print(cnt)