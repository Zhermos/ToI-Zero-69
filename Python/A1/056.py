import math
x,y,z = map(int,input().split())
X,Y,Z = map(int,input().split())
print(f"{(math.sqrt((X-x)**2+(Y-y)**2+(Z-z)**2)):.2f}")