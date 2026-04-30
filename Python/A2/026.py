n = int(input())
count = 0
name,weights = [],[]
for i in range(n):
    n,weight = map(str,input().split())
    if(int(weight)>15):count += 1
    name.append(n)
    weights.append(int(weight))
index = weights.index(max(weights))
print(f"{count}\n{name[index]} {max(weights)}")