from collections import deque
def bfs(adjList, startNode, visited):
    q = deque()
    visited[startNode] = True
    q.append(startNode)
    while q:
        currentNode = q.popleft()
        print(currentNode, end=" ")
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    vertices = 5

    adjList = [[] for _ in range(vertices)]

    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    visited = [False] * vertices
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    bfs(adjList, 0, visited)

if __name__ == "__main__":
    main()
