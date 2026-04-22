n =int(input())
isPrime = True
for i in range(2,int(n**0.5+1)):
    if(n%i==0):
        isPrime = False
        break
if(n==0 or n==1):isPrime = False
if(isPrime):
    print("Yes")
    for i in range(2,n+1):
        isPrime = True
        for j in range(2,int(i**0.5+1)):
            if(i%j==0):
                isPrime = False
                break
        if(isPrime):print(i,end=" ")
else:print("No")
    