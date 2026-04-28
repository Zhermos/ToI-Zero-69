original = input()
l = len(original)
begin = ord(original[0].upper())
end = ord(original[-1].upper())

lst = []


for i in range(1, 11):
    v_i = i - 1
    
    if i % 2 != 0:
        val = begin + v_i
    else:
        val = end - v_i
        
    rem = val % l
    
    if rem > 9:
        rem = rem % 10
        
    lst.append(rem)
ans = lst[2:8]
print(*ans)