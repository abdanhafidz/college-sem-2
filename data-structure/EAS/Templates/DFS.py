N,M= map(int,input().split())
visited = [0]*N
adj = [set() for _ in range(N+1)]
def dfs(start, to):
    if(start) == to:
        print("dah sampe")
    visited[start] = 1
    for neighbour in adj[start]:
        if(not visited[neighbour]):
            # Works
            dfs(neighbour, to)
for _ in range(M):
    U,V = map(int, input().split())
    adj[U].add(V)
    adj[V].add(U)

print(adj[1])