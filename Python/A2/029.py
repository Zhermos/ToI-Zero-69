n = int(input())
for i in range(n):
    for j in range(n):
        if(i>1 and i<n-1 and j!=0 and j!=i and j<=i):print(1,end=" ")
        elif(j<=i):print(0,end=" ")
    print("")