

 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node

 
# A utility function to insert
# a new node with the given key in BST

 
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
nodes = [set() for _ in range(1000)]
node = set()
def printCurrentLevel(root, level):
    
    if root is None:
        return
    if level == 1:
        node.add(root.key)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
    return node
# Inserting nodes
i = 0
root = None

while(True):
    x = list(map(int,input().split()))
    if(x[0] == 1):
        root = insert(root, x[1])
        height = maxDepth(root)
        nodes[height] = (printCurrentLevel(root,height - 1))
    elif(x[0] == 2):
        M = x[1]
        height = maxDepth(root)
        if(M > height - 1):
            print(f"kedalaman maksimumnya {height - 1} oi")
        else:
            print(len(nodes[M]) // M)
    elif(x[[0] == -1]):
        break
