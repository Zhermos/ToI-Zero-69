n = int(input())
money = [1000,500,100]
if(100<=n<=20000 and n%100==0):
    for i in money:
        if(int(n/i)!=0):
            print(f"{i} = {int(n/i)}")
            n%=i
else:print("ERROR") 