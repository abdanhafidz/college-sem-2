t = int(input())

for _ in range(t):
    n = int(input())
    stack = []
    s = input()
    for x in s:
        if(not stack):
            stack.append(x)
        else:
            crnt = stack[-1]
            if(x != crnt):
                stack.pop()
            else:
                stack.append(x)
    print(len(stack))
