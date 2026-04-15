lst = list(map(int,input().split()))
result = ""
for i in lst:
    if(i==0):result+="-"
    if(i//1000!=0):
        result+="#"
        i%=1000
    if(i//100!=0):
        result+="/"
        i%=100
    if(i//10!=0):
        result+="+"
        i%=10
    if(i//1!=0):
        result+="*"
print(result)