t = int(input())
for _ in range(t):
    n = int(input())
    freq = [0*n]
    for _ in range(n):
        u,v = map(int,input().split())
        freq[u - 1]+=1
        freq[v - 1]+=1
    res = 0
    for x in freq:
        if(x == 1): res+=1
    print((res+1)//2)



