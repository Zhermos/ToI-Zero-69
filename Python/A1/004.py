lst = [5,20,25]
if all(int(input()) >= i for i in lst):
    print("pass")
else:
    print("fail")