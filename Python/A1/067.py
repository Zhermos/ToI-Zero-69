member,n,sum = str(input()),int(input()),0
for i in range(n):
    A = float(input())
    sum += A
if(member == "Y"):print(f"{(sum*95/100):.2f}")
elif(member == "N" and sum>=500):print(f"{(sum*97/100):.2f}")
else:print(f"{(sum):.2f}")
