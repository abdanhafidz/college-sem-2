class HashTable:
    def __setitem__(self, key, value):
        self.put(key, value)
    def __getitem__(self, key):
        return self.get(key)

ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"
for key in ("good", "better", "best", "worst", "ad", "ga"):
 v = ht[key]
 print(v)
print("The number of elements is: {}".format(ht.count))