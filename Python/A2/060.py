n = int(input())
lst = []
for _ in range(n):
    A = list(map(int,input().split()))
    lst.append(A)
found = False
for tx in range(1,1000):
    for ty in range(1,1000):
        match = True
        for x,y,d in lst:
            if(tx-x)**2 + (ty-y)**2 != d**2:
                match = False
                break

        if match:
            print(f"{tx} {ty}")
            found = True
            break

    if(found):
        break
    