n = int(input())
count = 0
for i in range(n):
    A = input()
    if(A in ['A','E','I','O','U']):count += 1 
print(count)