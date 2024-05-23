N,M= map(int,input().split())
visited = [0]*N
adj = [set() for _ in range(N+1)]
def dfs(x,step):
    visited[x] = 1
    max = 0
    for con in adj[x]:
        if( visited[con] != 1 ):
           step+=1
           if(dfs(con,step) > max):
               max = dfs(con,1)
    step+=max
    return step
# print(adj)
for _ in range(M):
    U,V = map(int, input().split())
    adj[U].add(V)
    # print(U)
    # print(adj[U])
    # print(adj[V])
    adj[V].add(U)
    # print(V)
    # print(adj[V])
    # print(adj[U])
x = int(input())

print(dfs(x,1) + 1)


