A = input()
result = ""
n = [int(A[0]),int(A[1]),int(A[2]),int(A[3]),int(A[4])]
if(n[0] > 5): result += "9"
elif(n[1] > 5): result += "10"
elif(n[2] > 5): result += "11"
elif(n[3] > 5): result += "12"
elif(n[4] > 5): result += "14"
else: result += "13"

if(A==A[::-1]):
    if(n[0]+n[4]>5): result += "1"
    elif(n[1]*n[3]>5): result += "2"
    else: result += "0"
else:
    if(n[4]//n[1]>5): result += "1"
    elif(n[1]-n[4]>5): result += "2"
    else: result += "0"
if(sum(n)>25): result += "1"
elif(n[0]*n[1]*n[2]*n[3]*n[4]>55): result += "2"
else: result += "0"
print(result)
