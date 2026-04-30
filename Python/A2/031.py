d = int(input())
DNA = [list(map(str,input().split()))for _ in range(2)]
miss = 0
n = int(input())
for i in range(n):
    command = list(map(str,input().split()))
    DNA[(int(command[0]))-1][(int(command[1]))] = command[2]
for i in range(d):
    if((DNA[0][i] == "A" and DNA[1][i] == "T") or (DNA[1][i] == "A" and DNA[0][i] == "T")):pass
    elif((DNA[0][i] == "C" and DNA[1][i] == "G") or (DNA[1][i] == "C" and DNA[0][i] == "G")):pass
    else:miss+=1
for i in DNA:
    print(*i)
print(miss)