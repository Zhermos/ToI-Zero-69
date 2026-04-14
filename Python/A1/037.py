n = int(input())
value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
result = ""
for i in range(0,13):
    while(n >= value[i]):
        n -= value[i]
        result += symbols[i]
print(result)