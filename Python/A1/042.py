A = input()
x,y = 0,0
for move in A:
    if move == "N":
        y += 1
    elif move == "S":
        y -= 1
    elif move == "E":
        x += 1
    elif move == "W":
        x -= 1
print(f"{x} {y} {abs(x) + abs(y)}")