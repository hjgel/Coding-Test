B = input()
G = input()
li = []
alpha = {'A' : 3,'B' : 2, 'C' : 1, 'D' : 2, 'E' : 3, 'F' : 3, 'G' : 2, 'H' : 3, 'I' : 3, 'J' : 2, 'K' : 2, 'L' : 1, 'M' : 2, 'N' : 2, 'O' : 1, 'P' : 2, 'Q' : 2, 'R' :2, 'S' : 1, 'T' : 2, 'U': 1, 'V' : 1, 'W': 1,'X':2,'Y':2,'Z':1}


def love(love_li):
    while len(love_li) != 2:
        for i in range(0, len(love_li) - 1):
            love_li[i] = love_li[i] + love_li[i+1]
            if love_li[i] >= 10:
                love_li[i] -= 10
        del love_li[len(love_li)-1]
    return love_li

for i in range(len(B)):
    li.append(alpha[B[i]])
    li.append(alpha[G[i]])

result = love(li)
print(str((result[0])) + str(result[1]))