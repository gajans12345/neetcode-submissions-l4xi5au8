# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax = root.val

        def dfs(root):
            l = 0
            r = 0
            nonlocal globalMax
            if root.left:
                l = max(dfs(root.left),0)
            if root.right:
                r = max(dfs(root.right),0)
            globalMax = max(l + r + root.val,globalMax)
            return max(l,r) + root.val




        dfs(root)
        return globalMax
        