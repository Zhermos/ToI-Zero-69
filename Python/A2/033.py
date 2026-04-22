time = [60,120,180,240,300,360,1440]
price = [25,50,80,110,145,180,250]
check = True
INhr,INmin = map(str,input().split("."))
OUThr,OUTmin = map(str,input().split("."))
IN,OUT = (int(INhr)*60)+int(INmin),(int(OUThr)*60)+int(OUTmin)
if(int(INmin)>60 or int(OUTmin)>60 or IN>OUT):print("ERROR")
else:
    if(OUT-IN<=15):print("FREE")
    else:
        for i in range(7):
            if(OUT-IN==time[i]):
                print(price[i])
                check = False
                break
            elif(OUT-IN<time[i]):
                print(price[i])
                check = False
                break
        if(check):print("ERROR")
        
