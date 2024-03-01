# awas kau kalau nyontek ya
stack = []
n = int(input())
while(n):
    n-=1
    i,p = map(int,input().split())
    tup = (i,p)
    stack.append(tup)
stack.sort(key=lambda a: int(a[1]))
stack = stack[::-1]
s = int(input())
count = 0
# Ambigu : Kalau misalkan barangnya itu ada di paling atas
while(1):
    x = stack.pop()
    if(x[0] == s):
        print(count)
        break
    else:
        if(not stack):
            print("Barangnya gak ada beb")
            break
        count+=1
# not stack = kosong




