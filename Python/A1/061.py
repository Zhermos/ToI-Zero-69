r,x,y = map(int,input().split())
L = (x**2)+(y**2)
print("ON" if r**2==L else ("IN" if r**2>L else "OUT"))