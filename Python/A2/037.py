
n = int(input())
queue = []
emergency = []
for i in range(n):
    lst = list(map(str,input().split()))
    if(len(lst)==3):
        if(lst[2]=="emergency"):
            emergency.append(lst[1])
        else:
            queue.append(lst[1])
    elif(len(lst)==1):
        if(lst[0]=="SHOW"):
            if(len(queue)<1):print("EMPTY")
            else:
                print(*(emergency+queue))
        elif(lst[0]=="TREAT"):
            if(len(emergency) > 0):
                del emergency[0]
            elif(len(queue) > 0):
                del queue[0]
# print(emergency)
# print(queue)
