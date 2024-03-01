stack = []    
s = input()
pair = {
    "(":")",
    "{":"}",
    "[":"]"
}
status = True
for x in s:
    if(x == "(" or x == "{" or x == "["):
        stack.append(x)
    else:
        if not stack:
            status = False
            break
        cur_stack = stack.pop()
        if pair[cur_stack] != x:
            status = False
            break
if(status):
    print("VALID")
else:
    print("INVALID")
            