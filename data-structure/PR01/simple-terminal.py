stack = []
while(1):
    # print(stack)
    cmd = input()
    s = cmd.split()
    ord = s[0]
    match ord:
        case "stop":
            break
        case "append":
            stack.append(s[1])
        case "prepend":
            stack.insert(0,s[1])
        case "cp":
            a = int(s[1])
            b = int(s[2])
            stack.insert(b,stack[a])
        case "mv":
            a = int(s[1])
            b = int(s[2])
            temp = stack[a]
            del stack[a]
            stack.insert(b,temp)
        case "rm":
            a = int(s[1])
            del stack[a]
print(len(stack))
for x in stack:
    print(x)
