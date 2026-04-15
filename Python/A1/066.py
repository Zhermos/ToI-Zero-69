x,y = map(int,input().split())
total = 0
count = 0
while(total<y and x>0):
    total+=x
    x-=2
    count+=1
if(total>=y):print(count)
else:print(-1)
