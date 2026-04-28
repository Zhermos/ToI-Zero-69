n,p = map(int,input().split())
totalBadTiles,totalBadPoints,totalFine = 0,0,0
arr = []
for i in range(n):
    badTilesRow,badPointsRow = 0,0
    lst = list(map(int,input().split()))
    arr.append(lst)
    print(*lst,end="")
    for i in lst:
        if(i>0):
            badTilesRow+=1
            totalBadTiles+=1
        badPointsRow+=i
        totalBadPoints+=i
    print(f" {badTilesRow} {badPointsRow}",end="")
    print("")
TilesCol,PointsCol =[],[]
for i in range(n):
    badTilesCol,badPointsCol = 0,0
    for j in range(n):
        unit = arr[j][i]
        if(unit>0):badTilesCol+=1
        badPointsCol+=unit
    TilesCol.append(badTilesCol)
    PointsCol.append(badPointsCol)
print(*TilesCol)
print(*PointsCol)
print(f"{totalBadTiles} {totalBadPoints} {(totalBadPoints*p):.2f}")
