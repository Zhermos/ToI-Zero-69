n = int(input())
lst = []
for i in range(n):
    N = int(input())
    lst.append(N)
print(f"{sum(lst)}\n{max(lst)}\n{min(lst)}\n{((sum(lst))/n):.1f}")