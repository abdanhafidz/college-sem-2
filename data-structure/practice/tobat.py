Q = int(input())
beli = []

while(Q):
    q = input()
    q = q.split()
    if(q[0] == "BELI"):
        buku = q[1]
        beli.append(buku)
    elif(q[0] == "JUAL"):
        buku = q[1]
        idx = beli.index(buku)
        beli.pop(idx)
    elif(q[0] == "PRINT"):
        for x in beli:
            print(x)
        print('---')
    Q-=1