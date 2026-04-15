n = int(input())
for i in range(n):
    a,b,c = map(float,input().split())
    sum = a+b+c
    print(f"{sum:.1f}",end="")
    if(sum>50):print(",Overloaded",end="")
    if(a>20):print(",Check Type Plastic",end="")
    if(b>20):print(",Check Type Can",end="")
    if(c>20):print(",Check Type Glass",end="")
    print("")