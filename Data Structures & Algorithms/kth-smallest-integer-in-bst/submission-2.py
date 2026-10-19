# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = 0

        def dfs(root):
            nonlocal count, ans
            if root is None:
                return
            dfs(root.left)
            print(root.val,count)

            count-=1
            if count == 0:
                ans = root.val
            v = dfs(root.right)
        dfs(root)     
        return ans



        