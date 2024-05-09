s = input()
stack = []
status = False
for x in s:
    if(x == "S"):
        stack.append("S")
    elif x == "P":
        if(stack):
            stack.pop()
        else:
            print("TIDAK")
            exit()

if(not stack):
    print("YA")
else:
    print("TIDAK")