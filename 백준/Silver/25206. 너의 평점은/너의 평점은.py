
total = 0 # 몇학점 들었는지 저장.
rank = [] # 뭘 받았는 지 저장. 

for i in range(20):
    trach, to, ran = map(str, input().split())
    if ran != "P":
        total += float(to)
    if ran == "A+":
        rank.append((4.5 * float(to)))
    elif ran == "A0":
        rank.append((4.0 * float(to)))    
    elif ran == "B+":
        rank.append((3.5 * float(to)))
    elif ran == "B0":
        rank.append((3.0 * float(to)))
    elif ran == "C+":
        rank.append((2.5 * float(to)))
    elif ran == "C0":
        rank.append((2.0 * float(to)))
    elif ran == "D+":
        rank.append((1.5 * float(to)))
    elif ran == "D0":
        rank.append((1.0 * float(to)))
    elif ran == "F":
        rank.append((0.0 * float(to)))

print(round((sum(rank) / total), 6))
