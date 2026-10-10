# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        if root is None:
            return root
        while queue:
            temp1 = queue.popleft()
            if temp1.left:
                queue.append(temp1.left)
            if temp1.right:
                queue.append(temp1.right)
            l = temp1.left
            temp1.left = temp1.right
            temp1.right = l
            
        return root

            
        