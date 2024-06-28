import sys
from heapq import heappop, heappush
def DIJKSTRA(U, V, W, s):
    dist = [sys.maxsize] * (V + 1)
    visited = [False] * (V + 1)
    pred = [None] * (V + 1)

    dist[s] = 0
    pq = []
    heappush(pq, (0, s))
    
    while pq:
        minDist, u = heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        
        for v, weight in U[u]:
            if not visited[v] and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pred[v] = u
                heappush(pq, (dist[v], v))
    
    return dist, pred

def main():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    U = {i: [] for i in range(1, V + 1)}
    
    print("Enter the edges in the format (u, v, w):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        U[u].append((v, w))

    s = int(input("Enter the source node: "))
    distances, predecessors = DIJKSTRA(U, V, None, s)

    print("Distances from source node {}:".format(s))
    for i in range(1, V + 1):
        if distances[i] == sys.maxsize:
            print("Node {}: Unreachable".format(i))
        else:
            print("Node {}: {}".format(i, distances[i]))

    print("Predecessors in the shortest path tree:")
    for i in range(1, V + 1):
        print("Node {}: {}".format(i, predecessors[i]))
        
if __name__ == "__main__":
    main()
