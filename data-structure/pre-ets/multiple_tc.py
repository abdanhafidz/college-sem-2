t = int(input())

def solve(x,y):
    print(x + y)
for _ in range(t):
    x,y = map(int,input().split())
    solve(x,y)

