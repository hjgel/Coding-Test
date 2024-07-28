N, K = map(int, input().split())
hp = list(input())

cnt = 0

for i in range(len(hp)):
    if hp[i] == "P":
        for j in range(i-K, K+i+1):
            if 0 <= j < N and hp[j] == "H":
                cnt += 1
                hp[j] = "0"
                break
print(cnt)