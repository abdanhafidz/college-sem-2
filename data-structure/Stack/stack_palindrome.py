# AMAMA
# mid = 2
# pivot = A
# telusuri selama idx si x < mid
# AM
# A
# EFA
# pivot = F
# mid = 1
# E
# EEFAE
# E 
# EE
# E
# 
def isPalindrome(s):
    stack = []
    mid = (len(s)//2)+1
    pivot = s[mid]
    idx = 0
    for x in s:
        if(idx <= mid):
            stack.append(x)
        elif(x == pivot or idx>mid):
            if(not stack):
                return True
            stack.pop()
        idx+=1

s = input() 
if(isPalindrome(s)):
    print("YOI")
else:
    print("ORA")
