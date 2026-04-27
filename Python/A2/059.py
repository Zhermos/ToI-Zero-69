n,d = map(int,input().split())
max = 0
for _ in range(n):
    lst = list(map(int,input().split()))
    tag = lst[0]
    if(sum(lst[1:])>max):
        max = sum(lst)
        Top = lst[0]
    trend = "huh"
    if (lst[1]<lst[-1]):trend = "GROWING"
    elif (lst[1]>lst[-1]):trend = "DECLINING"
    elif (lst[1] == lst[-1]):trend = "STABLE"

    if(tag == 1):hashtag = "TechTrends"
    elif(tag == 2):hashtag = "EcoLife"
    elif(tag == 3):hashtag = "FoodieHeaven"
    elif(tag == 4):hashtag = "FashionWeek"
    elif(tag == 5):hashtag = "HealthyLiving"
    print(f"{hashtag}: {sum(lst[1:])} total, {(sum(lst[1:])/d):.2f} avg, {trend}")
if(Top == 1):Topperformer = "TechTrends"
elif(Top == 2):Topperformer = "EcoLife"
elif(Top == 3):Topperformer = "FoodieHeaven"
elif(Top == 4):Topperformer = "FashionWeek"
elif(Top == 5):Topperformer = "HealthyLiving"
print(f"Top performer: {Topperformer}")