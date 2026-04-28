N = int(input())
A = int(input())
total_time = N * A
if total_time == 0:
    print("No teaching")
else:
    if (total_time//60)==0:
        print(f"{total_time%60} minutes")
    elif (total_time%60)==0:
        print(f"{total_time//60} hours")
    else:
        print(f"{total_time//60} hours {total_time%60} minutes")