T = int(input())

def solve(y,x):
    parking = []
    j = int(input())
    for _ in range(j):
        m,k = map(int,input().split())
        parking.append((m,k))
        if(k<y):
            parking.pop()
    if(len(parking)<x):
        print("Pika Pika!")
    else:
        print("Pika Zzz")
for _ in range(T):
    y,x= map(int,input().split())
    solve(y,x)