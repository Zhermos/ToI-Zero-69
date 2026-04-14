A = int(input())
B = int(input())
if(A >= 1 and A <= 3):
    if(A == 3 and B >= 21):
        print("spring")
    else:
        print("winter")
elif(A >= 4 and A <= 6):
    if(A == 6 and B >= 21):
        print("summer")
    else:
        print("spring")
elif(A >= 7 and A <= 9):
    if(A == 9 and B >= 21):
        print("fall")
    else:
        print("summer")
else:   
    if(A == 12 and B >= 21):
        print("winter")
    else:
        print("fall")