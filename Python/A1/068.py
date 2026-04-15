n = int(input())
check = True
score = list(map(int,input().split()))
print(f"{(sum(score)/n):.1f}")
if((sum(score)/n)>=60):
    for i in score:
        if(i<50):
            print("FAIL")
            exit()
    print("PASS")
else:print("FAIL")