menu = [100,120,200,60]
sum = 0
n=0
while(n!=5):
    n = int(input())
    if(4>=n>=1):sum += menu[n-1]
print(f"Bye Bye\nTotal Calories: {sum}")