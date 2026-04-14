n = int(input())
result = ""
total = 0 
number = list(map(int, input().split()))
for i in range(0, n * 2, 2):
    A = number[i]
    B = number[i+1]
    bigger = A if A >= B else B
    result += str(bigger)
    total += bigger
    if(n==1):
        print(bigger)
        exit()
    if i < (n * 2) - 2:
        result += " + "
    else:
        result += " = "
result += str(total)
print(result)