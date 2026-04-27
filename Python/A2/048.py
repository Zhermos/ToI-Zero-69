n = int(input())
index = []
check = False
if(n!=0):
    lst = list(map(int,input().split()))
    print("Student: ",end="")
    print(" ".join(f"Student{i }" for i in range(1,n+1)))
    print(f"Highest score: {max(lst)}")
    print(f"Lowest score: {min(lst)}")
    print(f"Average score: {(sum(lst)/n):.1f}")
    print("Students who scored above average:")
    for idx in range(n):
        if lst[idx] > sum(lst)/n:
            print(f"Student {idx + 1}")
else:
    print("Student:")
    print("Highest score: 0")
    print("Lowest score: 0")
    print("Average score: 0.0")
    print("Students who scored above average:")