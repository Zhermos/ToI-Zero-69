start,stop = map(int,input().split())
lst = []
for i in range(start,stop+1):
    if i > 1:
        prime = True
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                prime = False
                break
        if(prime):
            lst.append(i)
print(*lst)
print(f"Total primes: {len(lst)}")
