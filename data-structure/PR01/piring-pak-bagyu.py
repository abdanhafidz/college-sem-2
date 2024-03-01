n = int(input())
stack = []
for _ in range(n):
    cmd = input()
    s = cmd.split()
    if(s[0] == "add"):
        x = int(s[1])
        y = int(s[2])
        for _ in range(y):
            stack.append(x)
        print(len(stack))
    elif(s[0] == "del"):
        x = int(s[1])
        for i in range(0,x):
            ret = int(stack.pop())
            if(i == 0):print(ret)
    elif(s[0] == "adx"):
        stack = [k+int(s[1]) for k in stack ]
    elif(s[0] == "mux"):
        stack = [k*int(s[1]) for k in stack ]
    elif(s[0] == "dex"):
        stack = [k-int(s[1]) for k in stack ]
        
    

