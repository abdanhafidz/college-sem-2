class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def get_quadratic(self, key):
        h = self._hash(key)
        j = 1
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * j) % self.size
            j += 1
        return None

    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h + j * j) % self.size
            j += 1
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def check_growth(self):
        load_factor = self.count / self.size
        if load_factor > 0.7:
            self._resize()

    def _resize(self):
        old_slots = self.slots
        new_size = self.size * 2
        self.size = new_size
        self.slots = [None] * new_size
        self.count = 0

        for item in old_slots:
            if item is not None:
                self.put_quadratic(item.key, item.value)

# Contoh penggunaan
hash_table = HashTable(10)
hash_table.put_quadratic("key1", "value1")
hash_table.put_quadratic("key2", "value2")
print(hash_table.get_quadratic("key1"))  # Output: value1
print(hash_table.get_quadratic("key2"))  # Output: value2
print(hash_table.get_quadratic("key3"))  # Output: None
