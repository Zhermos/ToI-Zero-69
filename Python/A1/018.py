A = int(input())
switch = {
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"
}
if(A<0):print("Error : Please input positive number")
elif(A==0 or A>=10):print("Error : Out of range")
else:
    print(switch[A])