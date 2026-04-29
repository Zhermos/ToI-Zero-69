lst = []
result = []
while(True):
    huh = list(map(int,input().split()))
    lst.append(huh)
    if(huh[-1]) == 0:break
for i in range(len(lst)-1):
    if(lst[i][1] == lst[i+1][0]):
        x = "P"
    else: x = "X"
    result.append(f"{i+1}{x}")
result.reverse()
for i in result:
    print(i)
