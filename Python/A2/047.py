n = int(input())
for _ in range(n):
    line = input().strip()
    raw = line.lower().split()
    clean = [x.strip(",.!?") for x in raw]
    lens = sum(len(x) for x in raw)

    if("hello" in clean or "hi" in clean):print("Hello! How can I help you?")
    elif("bye" in clean or "goodbye" in clean):print("Goodbye! Have a nice day!")
    elif(raw[-1][-1] == "?"):print("That's an interesting question!")
    elif(any(z.isdigit() for z in line)):print("I see some numbers there!")
    elif(lens >= 20):print("That's quite a long message!")
    else:print("I understand.")
