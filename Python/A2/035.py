def Permutation(lst):
    if(len(lst)<=1):
        return[lst]
    result = []

    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i]+lst[i+1:]
        for j in Permutation(remaining):
            result.append([current]+j)
    return result
n = int(input())
ls = [str(input()) for _ in range(n)]
for sub in Permutation(ls):
    print(*sub)
print(len(Permutation(ls)))