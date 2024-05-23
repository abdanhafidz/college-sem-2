matrix = []
n,m = map(int,input().split())
for i in range(n):
    elemen = list(input())
    matrix.append(elemen)
visited = [[0]*m for _ in range(n)]
def dfs(x,y):
    if (x < 0 or y < 0 or x > (n - 1) or y > (m - 1) or visited[x][y] == 1 or matrix[x][y] == "#"):
       return
    else:
        visited[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
# dfs(3,3) [Visited[3][3] = 1] -> dfs(2,3) [Visited[2][3] = 1]
# defs(2,3) -> dfs(1,3) [Vis[1][3] = 1] , -, dfs(2,2) [Vis[2][2] = 1]

count = 0
for i in range(0,n):
    for j in range(0,m):
        if visited[i][j] == 1 or matrix[i][j] == "#":
            continue
        dfs(i,j)
        count+= 1
print(count)