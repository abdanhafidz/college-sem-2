class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        currSum = 0

        def dfs(node):
            nonlocal currSum
            if node.right:
                dfs(node.right)

            currSum += node.val
            node.val = currSum

            if node.left:
                dfs(node.left)

        dfs(root)

        return root
        