N = input()
li = N.split("-")

idxZero = sum(map(int, (li[0].split('+'))))


for i in li[1:]:
    x = sum(map(int, (i.split('+'))))
    idxZero -= x
    
print(idxZero)
