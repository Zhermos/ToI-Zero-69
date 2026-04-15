N = int(input())
A = int(input())

total_time = N * A

if total_time == 0:
    print("No teaching")
else:
    hours = total_time // 60
    minute = total_time % 60
    
    if hours > 0 and minute > 0:
        print(f"{hours} hours {minute} minute")
    elif hours > 0:
        print(f"{hours} hours")
    else:
        print(f"{minute} minute")