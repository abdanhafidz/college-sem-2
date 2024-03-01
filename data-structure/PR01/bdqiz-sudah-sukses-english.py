
toko1 = []
toko2 = []
status = 2
while(1):
        cmd = input()
        cmd = cmd.split()
        msg = cmd[0]
        if(msg == "TUKAR"):
            if(status == 1):
                status = 2
            elif(status == 2):
                status = 1
        elif(msg == "CURI"):
            if(status == 1):
                if(not toko2):
                     print("TOKO 2 KOSONG")
                else:
                    toko1.append(toko2.pop())
            elif(status == 2):
                 if(not toko1):
                     print("TOKO 1 KOSONG")
                 else:
                      toko2.append(toko1.pop())
        elif(msg == "PESAN" and status == 2):
            ID = int(cmd[1])
            pesanan = int(cmd[2])
            tup = (ID,pesanan)
            toko2.append(tup)
        elif(msg == "PESAN" and status == 1):
            ID = int(cmd[1])
            pesanan = int(cmd[2])
            tup = (ID,pesanan)
            toko1.append(tup)
        elif(msg == "TUTUP"):
             uToko1 = 0
             uToko2 = 0
             if(not toko1):
                  print("TOKO 1 SEPI :(")
                  print("TOKO 1 UNTUNG : 0")
             else:
                  print("TOKO 1 :")
                  for x in toko1:
                      print(x[0],x[1])
                      uToko1 += x[1]  
                  print("TOKO 1 UNTUNG :",uToko1)
             if(not toko2):
                  print("TOKO 2 SEPI :(")
                  print("TOKO 2 UNTUNG : 0")
             else:
                  print("TOKO 2 :")
                  for x in toko2:
                      print(x[0],x[1])
                      uToko2 += x[1]  
                  print("TOKO 2 UNTUNG :",uToko2)
                  


