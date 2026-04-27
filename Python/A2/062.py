vowel = ["a","e","i","o","u"]
word = str(input().replace(" ","").lower())
a,e,i,o,u = 0,0,0,0,0
for j in word:
    if(j in vowel):
        if(j == "a"):a+=1
        elif(j == "e"):e+=1
        elif(j == "i"):i+=1
        elif(j == "o"):o+=1
        elif(j == "u"):u+=1
if(a>0):print(f"a: {a}")
if(e>0):print(f"e: {e}")
if(i>0):print(f"i: {i}")
if(o>0):print(f"o: {o}")
if(u>0):print(f"u: {u}")