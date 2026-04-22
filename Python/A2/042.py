command = ""
stock = {}
result = []
while(True):
    command = list(map(str,input().split()))
    action = command[0]
    if(action == "ADD"):
        if(command[1] not in stock):
            stock[command[1]] = 0
        stock[command[1]] += int(command[2])
    elif(action == "REMOVE"):
        if(command[1] in stock):
            stock[command[1]] -= int(command[2])
            if(int(command[2])>stock[command[1]]):result.append(f"Not enough stock for {command[1]}")
            if(stock[command[1]]<=0):
                stock.pop(command[1])
    elif(action == "CHECK"):
        lowstock = sorted([k for k, v in stock.items() if v < 5], key=lambda x: stock[x]) #IDK how it work
        if(len(lowstock)==0):
            result.append("All stocks are sufficient")
        else:
            for x in lowstock:
                result.append(x)
    elif(action == "REPORT"):
        report_keys = sorted(stock.keys(), key=lambda x: stock[x])
        report = [f"{k}: {stock[k]}" for k in report_keys]
        for x in report:
            result.append(x)
    elif(action == "END"):
        break
for i in result:
    print(i)


