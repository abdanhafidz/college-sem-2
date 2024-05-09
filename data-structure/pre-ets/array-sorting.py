arr = [(9,7),(2,8),(3,2),(2,2)]
arr.sort(key=lambda a: int(a[1]))
arr[::-1]
print(arr)

kotor  = [i for i in range(10,0,-1)]
print(kotor)