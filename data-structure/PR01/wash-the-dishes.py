# kotor = [5,4,3,2,1]
# ambil 3 kotor sabunin -> kotor = [5,4] sabun = [1,2,3] bersih =[]
# ambil 2 udah disabunin masukkin ke bersih -> kotor = [5,4] sabun = [1] bersih = [3,2]
# ambil 4 kotor terus sabunin -> kotor = [] sabun = [1,4,5] bersih = [3,2]
# ambil 3 udah disabunin masukkin ke bersih -> kotor = [] sabun = [] bersih = [3,2,5,4,1]
# urutan dari atas ke bawah piring bersih = [1,4,5,2,3]

N = int(input())
M = int(input())
kotor  = [i for i in range(N,0,-1)]
sabun  = []
bersih = []
for _ in range(M):
    C,D = map(int,input().split())
    if(C == 1):
        for _ in range(D):
            if(kotor):
                x = kotor.pop()
                sabun.append(x)
            else:
                break
    elif(C == 2):
        for _ in range(D):
            if(sabun):
                x = sabun.pop()
                bersih.append(x)
            else:
                break
# print(kotor,sabun,bersih)
for i in range(0,N):
    if(i == 0 and not kotor):
        print("-","\t",end="")
    else:
        if(not kotor):
            print("","\t",end="")
        else:
            print(kotor.pop(),"\t",end="")
    if(i == 0 and not sabun):
        print("-","\t",end="")
    else:
        if(not sabun):
            print("","\t",end="")
        else:
            print(sabun.pop(),"\t",end="")
    if(i == 0 and not bersih):
        print("-","\t",end="")
    else:
        if(not bersih):
            print("","\t",end="")
        else:
            print(bersih.pop(),"\t",end="")
    print()
