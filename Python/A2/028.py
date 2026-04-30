n = int(input())
miss = 0
lst = [list(input()) for _ in range(2)]
for i in range(n):
    if(int(lst[0][i]) + int(lst[1][i]) == 9):
        pass
    else:
        miss+=1
if(miss>0):
    print(f"NO {miss}")
else:
    print("YES")
