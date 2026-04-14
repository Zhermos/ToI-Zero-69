year,cc = int(input()),int(input())
y = 0 if(year<=1990)else(1 if(year<=1999)else 2)
c = 0 if(cc<=1500)else(1 if(cc<=2000)else 2)
table = [
    [1250,1400,2000],
    [1100,1300,1700],
    [1000,1200,1500]
]
print(table[y][c])