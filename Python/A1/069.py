I,J = int(input()),int(input())
for i in range(I):
    for j in range(J):
        if(I%2==0):
            if(i<I/2):print("A",end=" ")
            else:print("K",end=" ")
        else:
            if(i<=I//2):print("A",end=" ")
            elif(i>I//2):print("K",end=" ")
    print("")