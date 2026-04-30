L,P = map(int,input().split())
R,M,F = map(int,input().split())
R1,M1,F1 = 0,0,0
lst = []
for i in range(P):
    Length,Point = map(int,input().split())
    if(Length%R==0):R1+=Point
    if(Length%M==0):M1+=Point
    if(Length%F==0):F1+=Point
results = {'Rabbit': R1, 'Monkey': M1, 'Frog': F1}
max_score = max(results.values())
winners = [name for name, score in results.items() if score == max_score]
for name in winners:
    print(f"{name} {max_score}")
