T = int(input())
for _ in range(T):
    L = list(map(int,input().split()))
    x = len(L)
    L = L[0:x-1]
    J = list(map(int,input().split()))
    y = len(J)
    J = J[0:y-1]
    res = 0
    for j in range(0,len(L)):
        curL = L[j]
        cur_min = J[0]
        for i in range(1,len(J)):
            sel = abs(curL - J[i])
            if(sel > abs(curL - cur_min)):
                cur_min = J[i]
        idx = J.index(cur_min)
        J.pop(idx)
        res += abs(curL - cur_min)
    print(res)



