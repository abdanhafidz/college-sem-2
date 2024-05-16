N = int(input())
minCost = [ [None]*(N*N)]
Cost = [ [0]*(N*N)]
adj = [ []*(N*N)]
Q = int(input())
solved = []
def solve(start, to):
        if((start in solved) or (to in solved)):
             return
        for con in adj[start]:
            cur = Cost[start][con] + solve(con,to)
            if(cur < minCost[start][to] and minCost[start][to] != None and (con not in solved) ):
                 minCost[start][to] = cur
        solved.push(0,start)
        return minCost[start][to]
for _ in range(Q):
    U,V,cost = map(int, input.split())
    adj[U].append(V)
    adj[V].append(U)
    Cost[U][V] = cost
    Cost[V][U] = cost
    
    


