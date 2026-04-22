n = int(input())
result = []
cave = list(map(int,input().split()))
player = cave.index(1)
chest = cave.index(2)
borderLeft = 0
borderRight = len(cave)-1
command = str(input())
for control in command:
    if(player == chest):
        break
    elif(control == "L"):
        if(player-1<borderLeft):
            player = borderLeft
        else:
            player -= 1
    elif(control == "R"):
        if(player+1>borderRight):
            player = borderRight
        else:
            player += 1
for i in range(len(cave)):
    if(player == chest):
        if(i == player):result.append(1)
        else:result.append(0)
    else:
        if(i == chest):result.append(2)
        elif(i == player):result.append(1)
        else:result.append(0)
print(*result)
        