cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

N = input()

for c in cro:
    N = N.replace(c, "*")

print(len(N))
