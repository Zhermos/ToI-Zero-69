even,odd = 0,0
for i in range(3):
    A = int(input())
    if A%2==0:even += 1 
    else: odd += 1
print(f"even {even}\nodd {odd}")