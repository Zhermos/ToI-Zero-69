grid = [list(map(int,input().split()))for _ in range(5)]
row,col = [],[]
checkR,checkC = True,True
for i in range(5):
    r,c = 0,0
    for j in range(5):
        r += grid[i][j]
        c += grid[j][i]
    row.append(r)
    col.append(c)
for i in range(5):
    if(row[i]%2!=0):
        print(i,end=" ")
        checkR = False
if(checkR):print(-1,end=" ")
for i in range(5):
    if(col[i]%2!=0):
        print(i,end=" ")
        checkR = False
if(checkR):print(-1,end=" ")


