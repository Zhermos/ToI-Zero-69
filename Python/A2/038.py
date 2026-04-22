n = int(input())
sum,F,W,E = 0,0,0,0
for _ in range(n):
    F1,W1,E1,F2,W2,E2 = map(int,input().split())
    if(F1+W1+E1>=F2+W2+E2):
        sum+=F1+W1+E1
        F+=F1
        W+=W1
        E+=E1
    else:
        sum+=F2+W2+E2
        F+=F2
        W+=W2
        E+=E2
print(f"{sum}\n{F} {W} {E}\nYES"if(F>W+E)else f"{sum}\n{F} {W} {E}\nNO")
