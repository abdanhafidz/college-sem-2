class HashItem:
    def __init__(self, key, value) :
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for _ in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65
        self.prime_num = 5

    def _hash(self, key):
        # Fungsi hash pertama
        return hash(key) % self.size

    def h2(self, key):
        # Fungsi hash kedua
        return 1 + (hash(key) % (self.size - 1))

    def put_double_hashing(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
            j += 1
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get_double_hashing(self, key):
        h = self._hash(key)
        j = 1
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size
            j += 1
        return None

    def check_growth(self):
        load_factor = self.count / self.size
        if load_factor > self.MAXLOADFACTOR:
            self._resize()

    def _resize(self):
        old_slots = self.slots
        new_size = self.size * 2
        self.size = new_size
        self.slots = [None] * new_size
        self.count = 0

        for item in old_slots:
            if item is not None:
                self.put_double_hashing(item.key, item.value)

# Contoh penggunaan
hash_table = HashTable()
hash_table.put_double_hashing("key1", "value1")
hash_table.put_double_hashing("key2", "value2")
print(hash_table.get_double_hashing("key1"))  # Output: value1
print(hash_table.get_double_hashing("key2"))  # Output: value2
print(hash_table.get_double_hashing("key3"))  # Output: None
