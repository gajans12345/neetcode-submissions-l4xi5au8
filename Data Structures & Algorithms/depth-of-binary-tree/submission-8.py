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
        curDepth = 0
        maxDepth = 1
        queue.append([root,0])
        while queue:
            element = queue.popleft()
            curNode = element[0]
            curDepth = element[1]
            if curNode.left:
                queue.append([curNode.left,curDepth+1])
            if curNode.right:
                queue.append([curNode.right,curDepth+1])
            maxDepth = max(maxDepth,curDepth + 1)
        return maxDepth
            
        