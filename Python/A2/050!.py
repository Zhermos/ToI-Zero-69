n = input()
c = n[-1].upper()
integer = int(n[:-1])

if integer % 2 == 0:
    mid_left = (integer // 2) - 1
    mid_right = integer // 2
    max_dist = (integer // 2) - 1 
else:
    mid_left = integer // 2
    mid_right = integer // 2
    max_dist = integer // 2

for i in range(integer):
    if i < (integer // 2):
        dist = i
    else:
        dist = (integer - 1) - i
    if c == "#":
        char_to_print = "#"
    else:
        diff = max_dist - dist
        pos = (ord(c) - ord('A') + diff) % 50
        if pos > 25:
            real_pos = 50 - pos
        else:
            real_pos = pos
        char_to_print = chr(ord('A') + real_pos)
    for j in range(integer):
        if j == (mid_left - dist) or j == (mid_right + dist):
            print(char_to_print, end="")
        else:
            print("-", end="")
    print("")