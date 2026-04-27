n = int(input())
lst = list(map(float,input().split()))
sort = sorted(lst)
if n % 2 == 0:
    median = (sort[n // 2] + sort[n // 2 - 1]) / 2
else:
    median = sort[n // 2]
count = 0
for i in lst:
    if(i>=37):count+=1
print(f"SUM={sum(lst):.2f}")
print(f"AVG={(sum(lst))/n:.2f}")
print(f"MEDIAN={median:.2f}")               
print(f"MAX={max(lst):.2f}")
print(f"MIN={min(lst):.2f}")
print(f"ALERT={count}")
print("SORTED=" + " ".join([f"{x:.2f}" for x in sort]))
