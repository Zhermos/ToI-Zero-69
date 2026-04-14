sum,even,odd=0,0,0
n = int(input())
lst = list(map(int,input().split()))
for i in range(n):
    sum += lst[i]
    if(lst[i]%2==0):even+=1
    else:odd+=1
print(f"SUM {sum}\nEVEN {even}\nODD {odd}")