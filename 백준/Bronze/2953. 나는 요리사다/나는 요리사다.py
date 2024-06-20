Array_List = [list(map(int, input().split())) for _ in range(5)]
idx = 0
max_idx = 0

for i in range(len(Array_List)):
    if max_idx < sum(Array_List[i]): 
        max_idx = sum(Array_List[i])
        idx = i + 1

print(idx, max_idx)