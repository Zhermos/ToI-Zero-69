teams = {"CHE":0,"LIV":0,"MUN":0,"NEW":0}
match = [("CHE","LIV"),("CHE","MUN"),("CHE","NEW"),("LIV","MUN"),("LIV","NEW"),("MUN","NEW")]
for i in range(6):
    left,right = map(int,input().split())
    l,r = match[i]
    if(left > right):teams[l] += 3
    elif(left < right):teams[r] += 3
    elif(left == right):
        teams[l] += 1
        teams[r] += 1
sort = sorted(teams.items(), key=lambda x: (-x[1], x[0]))
for i in range(4):
    team_name = sort[i][0]
    score = sort[i][1]
    print(f"{i+1}. {team_name} {score}")
