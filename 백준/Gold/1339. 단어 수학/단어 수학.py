import sys
input = sys.stdin.readline

al_dict = {}
al_li = [] # 알파벳을 숫자로 환산한 값을 담을 리스트
KLi = [] # 알파벳을 담을 리스트
result = 0 # 더한 값을 보기 위한 수

N = int(input())

for i in range(65, 91):
    al_dict[chr(i)] = 0

for i in range(N):
    KLi.append(input().strip()) # N줄만큼 걸러서 리스트에 담음 

for alpha in KLi: # 담긴 문자열을 뽑아서 
    for c in range(len(alpha)): # 하나하나 다 봄. 
        num = 10 ** (len(alpha) - c - 1) # num = 10^2 .. num = 10^1.. num = 10^0
        al_dict[alpha[c]] += num # al_dict['A'] += 100 .. 110.. 111.. 211.. 221... 222

for val in al_dict.values(): # 값을 뽑아본다. 
    if val > 0 : # dict 값이 0보다 클 경우만 가동. 
        al_li.append(val) # al_li에 추가

al_li.sort(reverse=True) # 내림차순으로 sort해줌. 이유는 큰 수부터 보기 위함. 
for i in range(len(al_li)): # 리스트에 들어간 만큼 돌리고 
    result += al_li[i] * (9 - i) # 0번째 인덱스부터 * 9, 다음 8.. 이렇게 줌. 단위마다 크기가 정해지기 때문,.

print(result)