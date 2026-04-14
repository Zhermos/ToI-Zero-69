A = int(input())
# print(f"10 = {int(A/10)}")
# print(f"5 = {int(A%10/5)}")
# print(f"2 = {int(A%10%5/2)}")
# print(f"1 = {int(A%10%5%2/1)}") 
coins = [10,5,2,1]
for coin in coins:
    print(f"{coin} = {int(A/coin)}")
    A %= coin
