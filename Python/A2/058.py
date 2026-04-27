A,B,d,r = map(int,input().split())
c = 0
for i in  range(A,B+1):
    if(i%d==r):c+=1
print(c)
