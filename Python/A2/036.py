num,q = map(int,input().split())
start,stop = [],[]
result = []
for _ in range(num):
    a,b = map(int,input().split())
    start.append(a)
    stop.append(b)
query = list(map(int,input().split()))
for j in range(q):
    count = 0
    for i in range(num):
        if query[j] in range(start[i],(stop[i]+1)):count+=1
    result.append(count)
print(*result)

    