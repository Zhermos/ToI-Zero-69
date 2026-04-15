A = int(input())
B = A
sum = 0
if(A>=201):
    sum += 15*(A-200)
    A = 200
if(A>=101):
    sum += 12*(A-100)
    A = 100
if(A>=51):
    sum += 10*(A-50)
    A = 50
if(A>=11):
    sum += 7*(A-10)
    A = 10
if(A>=1):
    sum += 5*(A)
print(f"{(sum+(B*0.5)+(sum*0.07)):.2f}")