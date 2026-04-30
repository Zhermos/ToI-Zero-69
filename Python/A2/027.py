n = int(input())
count = 0
lst = [int(input()) for _ in range(n)]
for i in lst:
    if(max(lst) == i):count+=1
print(f"{max(lst)}\n{count}")