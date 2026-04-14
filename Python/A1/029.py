A = input()
vowel = ['a','e','i','o','u']
count = 0
for i in range(len(A)):
    if(A[i] in vowel):count+=1
print(count)