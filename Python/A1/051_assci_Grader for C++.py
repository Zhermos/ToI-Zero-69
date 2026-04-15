import sys
data = sys.stdin.read().split()
txt,n = data[0],int(data[1])
result = ""
for char in txt:
    result += chr((ord(char) - ord("a") + n) % 26 + ord("a"))
print(result)