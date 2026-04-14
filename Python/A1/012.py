A,B = int(input()),input()
C = int(str(A)[::-1])
print(f"{A} + {C} = {A+C}"if(B=="+")else f"{A} * {C} = {A*C}")