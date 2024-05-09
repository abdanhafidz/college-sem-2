buff = []
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data == self.data:
                print("Duplicate Value!")
        elif self.data != data:
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

n = int(input())
val = list(map(int, input().split()))

m = int(input())
root = Node(val[0])
i = 0
for p in val:
   if(i>0):
        root.insert(p)
   i+=1
while(m):
   cmd = input()
   a_cmd = cmd.split()[0]
   if(a_cmd == "insert"):
      key = int(cmd.split()[1])
      root.insert(key)
   if(a_cmd == "remove"):
      key = int(cmd.split()[1])
      root.remove(key)
   if(a_cmd == "inorder"):
      root.InorderPrint()
      print(" ".join(buff))
      buff = []
   if(a_cmd == "preorder"):
      root.PreorderPrint()
      print(" ".join(buff))
      buff = []
   if(a_cmd == "postorder"):
      root.PostorderPrint()
      print(" ".join(buff))
      buff = []
   m-=1
# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PreorderPrint()