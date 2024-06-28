import math
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
  
    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
  
    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 
  
            # Reassignment of node's parent 
            # to root node as 
            # path compression requires 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
  
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
  
        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1
  
    # The main function to construct MST 
    # using Kruskal's algorithm 
    def KruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V - 1: 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
  
        minimumCost = 0
        for u, v, weight in result: 
            minimumCost += weight 
        print(minimumCost) 

M = int(input())
g = Graph(M)
point = []
for _ in range(M):
    X,Y = map(int, input().split())
    point.append((X,Y))



for i in range(0,M):
    for j in range(0,M):
        C = math.floor(math.sqrt((point[i][0] - point[j][0])**2 + (point[i][1] - point[j][1])**2))
        if(i!=j):
            g.addEdge(i,j,C)
g.KruskalMST()
    

