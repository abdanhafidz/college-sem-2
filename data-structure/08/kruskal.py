class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def KRUSKAL(edgeList, V):
    ds = DisjointSet(V)
    edgeList.sort(key=lambda edge: edge[2])

    mst_cost = 0
    mst_edges = []

    for u, v, weight in edgeList:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges

def main():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    edgeList = []
    print("Enter the edges in the format (u, v, w):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edgeList.append((u, v, w))
    mst_cost, mst_edges = KRUSKAL(edgeList, V)
    print("Cost of the Minimum Spanning Tree:", mst_cost)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"({u}, {v}) - weight {weight}")

if __name__ == "__main__":
    main()
