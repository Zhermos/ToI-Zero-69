matrix1 = []
matrix2 = []
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    row = list(map(int,input().split()))
    matrix1.append(row)
for i in range(3):
    row = list(map(int,input().split()))
    matrix2.append(row)
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
for i in result:
    for j in i:
        print(j%32777,end=" ")
    print("")


