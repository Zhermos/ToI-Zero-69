Team,Member =  map(int,input().split())
res = 0
if(Team>10 or Team<1 or Member>20 or Member<1):
    print("Data Incorrect")
else:
    for i in range(Team):
        temp = list(map(int,input().split()))
        res += sum(temp)
        print(f"Team {i+1}: Average = {(sum(temp)/Member):.2f}, Max = {max(temp)}")
    print(f"Total Score of All Teams = {res}")