a,b,c = map(int,input().split())
print(a*25+b*40+c*55 if(a+b+c<3)else (a*25+b*40+c*55)*9//10)