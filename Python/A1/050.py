even,odd = 0,0
number = list(map(str,input().split()))
for i in number:
    if(int(i)>=0):
        if(int(i[-1])%2==0):even+=1
        else:odd+=1
print(f"{odd} {even} {odd+even}")
            