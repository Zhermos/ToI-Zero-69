age,day = input().split()
if(int(age)<5):print(0)
elif(int(age)<=18):print(50 if(day=="Wed")else 100)
elif(int(age)>=19):print(75 if(day=="Wed")else 150)