s = input()
stack = []
lay = 0
for x in s:
    if(x == "("):
        stack.append("(")
    else:
        if stack:
            stack.pop()
            if stack:
                lay+=1
            else:
                print("("*lay,")"*lay)
                lay=0
