# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return [0,0]
            if not node.left and not node.right: # base case
                return [node.val,0]
            left = [0,0]
            right = [0,0]
            if node.left:
                left = helper(node.left)
            if node.right:
                right = helper(node.right)
            
            return [max(left[0] + right[0],
                  node.val + left[1]+right[1]), left[0]+right[0]]

        return helper(root)[0]



        