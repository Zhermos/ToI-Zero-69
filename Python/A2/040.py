n = int(input())
matrix1 = []
matrix2 = []
result = []
for _ in range(n):
    lst = list(map(int,input().split()))
    matrix1.append(lst)
for _ in range(n):
    lst = list(map(int,input().split()))
    matrix2.append(lst)
for i in range(n):
    for j in range(n):
        result.append(matrix1[i][j]+matrix2[i][j])
for i in range(0,len(result),n):
    print(*result[i:i+n])
    
