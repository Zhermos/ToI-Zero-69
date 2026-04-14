A,B,C = input(),input(),input()
print(f"{A[:2]}{B[-1]}{C[-1]}"if(len(A)>5 and len(B)>5) else f"{A[0]}{C}{B[-1]}")