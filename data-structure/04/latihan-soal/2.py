buff = []
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def InorderPrint(self):
        if self.left:
            self.left.InorderPrint()
        buff.append(str(self.data)),
        if self.right:
            self.right.InorderPrint()

    def PreorderPrint(self):
        buff.append(str(self.data)),
        if self.left:
            self.left.PreorderPrint()
        if self.right:
            self.right.PreorderPrint()

    def PostorderPrint(self):
        if self.left:
            self.left.PostorderPrint()
        if self.right:
            self.right.PostorderPrint()
        buff.append(str(self.data)),

    def remove(self, key):
        if key < self.data:
            if self.left:
                self.left = self.left.remove(key)
            else:
                print("Cannot Find the Value!")
        elif key > self.data:
            if self.right:
                self.right = self.right.remove(key)
            else:
                print("Cannot Find the Value!")
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.remove(min_val)
        return self
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.data
    def sum_left_leaves(self):
            if self.left is None and self.right is None:
                return self.data if self == root.left else 0
            left_sum = self.left.sum_left_leaves() if self.left else 0
            right_sum = self.right.sum_left_leaves() if self.right else 0
            return left_sum + right_sum
n = int(input())
key = list(map(int,input().split()))
root = Node(key[0])
for x in key[1:]:
    root.insert(x)
print(root.sum_left_leaves())


