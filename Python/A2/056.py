n = int(input())
lst = list(map(int,input().split()))
array = [x for x in lst if(lst.count(x) == 1)]
s = sorted(array)
print(*s)