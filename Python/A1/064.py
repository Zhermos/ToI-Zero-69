lst = list(map(str,input().split()))
result = 0
for i in range(1,len(lst)):
    if(lst[i] == "+"):result+=10
    elif(lst[i] == "-"):result-=5
print(result)