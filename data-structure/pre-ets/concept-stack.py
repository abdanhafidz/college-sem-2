arr = [1,2,3,4,5,6,7,8]
stack = []
while(1):
    if arr:
        cur = arr.pop()
        stack.append(cur)
    else:
        break
print(arr)
print(stack)