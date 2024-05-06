den = int(input())
mol = 1

while den > mol:
    den -= mol
    mol += 1

if mol % 2 == 0:
    a = den
    b = mol - den + 1 
elif mol % 2 == 1:
    a = mol - den + 1
    b = den

print(f"{a}/{b}")