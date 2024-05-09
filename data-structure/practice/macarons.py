N = int(input())
m = list(map(str,input().split()))
T = int(input())
stack1 = m
stack2 = []
buff = []
for _ in range(T):
    cmd = input()
    cmd = cmd.split()
    if(cmd[0] == "PULL"):
        x = int(cmd[1])
        if(x > len(stack1)):
            print("Macaron Furina tidak sebanyak itu pls!")
        else:
            i = 1
            for _ in range(x):
                cur = stack1.pop()
                if(i == x):
                    stack2.append(cur)
                else:
                    buff.append(cur)
                i+=1
            stack1 = stack1 + buff
            buff = []
    elif(cmd[0] == "PUT"):
        balik = stack2[::-1]
        stack2 = []
        stack1 = stack1 + balik
    else:
        print("Apa itu? Furina tidak paham!")
vstack1 = " ".join(stack1)
vstack2 = " ".join(stack2)
print(vstack1)
print(vstack2)