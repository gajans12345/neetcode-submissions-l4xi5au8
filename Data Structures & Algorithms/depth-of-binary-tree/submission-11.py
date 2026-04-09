# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root is None:
            return 0
        
        queue.appendleft([root,1])
        maxDepth = 1
        prev = root
        while len(queue) != 0:
            v = queue.pop()
            maxDepth = max(maxDepth, v[1])
            if v[0].right:
                queue.appendleft([v[0].right,v[1]+1])
            if v[0].left:
                queue.appendleft([v[0].left,v[1]+1])
        return maxDepth 

            

        