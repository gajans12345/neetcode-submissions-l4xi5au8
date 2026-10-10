# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if root is None:
            return root
        stack.append(root)
        while stack:
            temp1 = stack.pop()
            if temp1.left:
                stack.append(temp1.left)
            if temp1.right:
                stack.append(temp1.right)
            l = temp1.left
            temp1.left = temp1.right
            temp1.right = l
            
        return root

            
        