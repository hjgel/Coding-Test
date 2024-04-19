from collections import Counter

N = input()
S = Counter(N)
cnt = 0
result = ""
hol_re = ""
keys = sorted(S.keys())
for key in keys:
    if S[key] % 2 != 0:
        cnt += 1
        hol_re += key
        S[key] -= 1
        if cnt == 2:
            break
    if S[key] % 2 == 0 and S[key] != 0:
        if S[key] >= 4:
            result += key * (S[key] //2)
        else :
            result += key

if cnt == 2: print("I'm Sorry Hansoo")
else : print(result + hol_re + result[::-1])