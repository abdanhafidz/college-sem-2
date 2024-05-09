class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, node):
    if node.val < root.val:
        if not root.left:
            root.left = node
        else:
            insert(root.left, node)
    elif node.val > root.val:
        if not root.right:
            root.right = node
        else:
            insert(root.right, node)

def findHeight(root) -> int:
    if not root:
        return -1
    left_height = findHeight(root.left)
    right_height = findHeight(root.right)
    return max(left_height, right_height) + 1

def buildTree(inputs):
    if not inputs:
        return None
    root = TreeNode(inputs.pop(0))
    for val in inputs:
        if val is not None:
            insert(root, TreeNode(val))
    return root

inputs = list(map(int, input().split()))
tree = buildTree(inputs)
print(findHeight(tree))
