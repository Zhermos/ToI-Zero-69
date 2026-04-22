lst = []
for i in range(1,4):
    n = int(input())
    lst.append(n)
    print(f"Input number {i} stored.")
x = int(input())
if(x==1):
    print(f"Original order: ",*lst)
elif(x==2):
    lst.sort(reverse=True)
    print(f"Descending order: ",*lst)
elif(x==3):
    lst.sort()
    print(f"Ascending order: ",*lst)
elif(x==0):
    pass