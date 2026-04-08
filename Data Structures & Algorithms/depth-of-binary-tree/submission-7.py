# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if not root:
            return 0
        stack.append([root,0])
        maxDepth = 1
        curDepth = 0
        curNode = root
        while stack:
            element = stack.pop()
            curDepth = element[1]
            print(element[0].val,element[1],curDepth)
            curNode = element[0]
            if curNode.left:
                stack.append([curNode.left,curDepth + 1])
            if curNode.right:
                stack.append([curNode.right,curDepth + 1])
            maxDepth = max(maxDepth,curDepth + 1)
            
        return maxDepth


