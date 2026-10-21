# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max depth -> dfs whilst tracking max depth
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            # popped as far depth from current node
            res = max(res, left + right)

            # furthest path of child nodes
            return 1 + max(left, right)
        
        dfs(root)
        return res