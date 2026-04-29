N,M = map(int,input().split())
total = []
directions = [
    (-1, -1),( 0, -1),( 1, -1),
    ( 1,  0),         (-1,  0),
    ( 1,  1),( 0,  1),(-1,  1),     
]
grid = [[0 for _ in range(M)]for _ in range(N)]
A = int(input())
lst1 = [list(map(int,input().split()))for _ in range(A)]
for w,s in lst1:
    grid[w][s] += 1
for x in range(M):
    for y in range(N):
        total1 = 0
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N:
                total1 += grid[ny][nx]
                total.append(total1)
print(max(total))