A,B = int(input()),input().lower()
if(B == 'c'):
    if(A<=0):print("solid")
    elif(A>=100):print("gas")
    else:print("liquid")
elif(B == 'f'):
    if(A<=32):print("solid")
    elif(A>=212):print("gas")
    else:print("liquid")