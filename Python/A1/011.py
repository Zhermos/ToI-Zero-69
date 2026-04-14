A = input()
result = ""
count = 1
for i in range(len(A)):
    if(i+1<len(A) and A[i] == A[i+1]):
        count+=1
    else:
        result += f"{count}{A[i]}"
        count=1
print(result)